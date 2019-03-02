import os
from flask import Flask, render_template, request, redirect, url_for, flash, \
send_from_directory
from flaskext.mysql import MySQL
from werkzeug.utils import secure_filename

mysql = MySQL()
UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SESSION_TYPE'] = 'filesystem'


@app.route("/")
def main():
  return "Hello, world!"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/upload_success')
def upload_successful():
  return render_template("upload_success.html")

@app.route('/upload', methods=['GET', 'POST'])
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
    return render_template("upload.html")

#
#@app.route('post/<variable>', methods=['GET'])
#def feedback_form(variable):
#  pass



if __name__ == "__main__":
    app.secret_key = os.urandom(32) # 128 bit randomn key
    app.run(debug=True, threaded=True, host='0.0.0.0')

