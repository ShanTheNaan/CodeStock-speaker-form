import os
import json
import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, \
send_from_directory, jsonify
from flaskext.mysql import MySQL
from werkzeug.utils import secure_filename
import mysql_helper

mysql = MySQL()
mysql_obj = mysql_helper.MySQLHelper()
UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SESSION_TYPE'] = 'filesystem'
app.config['MYSQL_DATABASE_USER'] = mysql_obj.get_username()
app.config['MYSQL_DATABASE_PASSWORD'] = mysql_obj.get_passwd() 
app.config['MYSQL_DATABASE_DB'] = mysql_obj.get_db()
app.config['MYSQL_DATABASE_HOST'] = mysql_obj.get_host()
mysql.init_app(app)

print(app.config['MYSQL_DATABASE_PASSWORD'])
@app.route("/")
def main():
  return render_template("index.html") 


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload_success')
def upload_successful():
  return render_template("upload_success.html")


@app.route('/admin', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        f = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if f.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if f and allowed_file(f.filename):
            # always overwrite to this file
            filename = 'talkInfo.csv' 
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect("/upload_success")
        else:
            flash('Incorrect File Type: Excpected .csv')

    return render_template("admin.html")


@app.route('/admin/speaker_comments')
def display_speaker_comments():
  return render_template("feedback_display.html")


@app.route('/feedback/<int:uid>', methods=['GET', 'POST'])
def give_feedback(uid):
  speakers = []
  query = "SELECT bt.TalkId, tt.EventTitle, st.FirstName, st.LastName FROM \
    bridge_table bt INNER JOIN talk_table tt ON tt.TalkId = bt.TalkId INNER JOIN \
    speaker_table st ON st.SpeakerId = bt.SpeakerId WHERE bt.TalkId=" + str(uid)

  if request.method == 'GET':
    rows = mysql_obj.query_db(query)
    talk_title = rows[0][1]
    for row in rows:
      speakers.append(row[-2] + ' ' + row[-1])

    return render_template("form.html", title=talk_title, speakers=speakers) 
  elif request.method == 'POST': # POST request
    mysql_obj.get_all_talks_for_user(uid)
    name = ''
    guest_email = ''
    guest_social_media = ''
    questions = ''
    speaker_rating = request.form['speaker-ratings']
    content_rating = request.form['content-ratings']
    comment = request.form['talk-comment']

    # optional
    name = request.form.get('guest-name')
    guest_email = request.form.get('guest-email')
    guest_social_media = request.form.get('guest-social-media')
    questions = request.form.get('questions')

    #print(name)

    #query = "SELECT COUNT(*) FROM user_table WHERE UserName=" + str(name) + ""
    #rows = mysql_obj.query_db(query)
    #for row in rows:
    #    print(row[0])

    return render_template("thanks.html")
  else:
    print('NO GET OR POST')


@app.route('/events')
def display_events():
  talkStuff = {}
  query = "SELECT bt.TalkId, tt.EventTitle, tt.EventLocation, tt.EventTime,\
    st.FirstName, st.LastName FROM bridge_table bt INNER JOIN talk_table tt \
    ON tt.TalkId = bt.TalkId INNER JOIN speaker_table st ON st.SpeakerId = bt.SpeakerId"
  rows = mysql_obj.query_db(query)
  prev_uid = -1
  for row in rows:
    if row[0] != prev_uid:
      talkStuff[row[0]] = [elem for elem in row[1:]]
      talkStuff[row[0]][-2] += ' ' + talkStuff[row[0]][-1]
      del talkStuff[row[0]][-1]
    else:
      talkStuff[row[0]].append(row[-2] + ' ' + row[-1])
    prev_uid = row[0]

  return jsonify(talkStuff)


@app.route('/qr')
def return_qr():
  return render_template("qrCode.html")


if __name__ == "__main__":
    app.secret_key = os.urandom(32) # 128 bit randomn key
    app.run(debug=True, threaded=True, host='0.0.0.0')

