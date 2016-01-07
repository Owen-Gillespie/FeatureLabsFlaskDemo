from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import models

@app.route("/")

def index():
    return render_template('index.html')

@app.route("/user/<username>")

def user_comments(username):
	#displays an analysis of the last 50 comments by a user

	return 'User %s' % username

if __name__ == "__main__":
    app.run()