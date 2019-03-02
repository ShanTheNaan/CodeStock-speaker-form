from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

@app.route("/")
def main():
  pass

@app.route('post/<variable>', methods=['GET'])
def feedback_form(variable):
  pass



if __name__ == "__main__":
    app.run()

