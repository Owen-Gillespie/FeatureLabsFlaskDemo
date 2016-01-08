from flask import render_template
from app import app
import comment_scraper

@app.route("/")

def index():
    return render_template('index.html')

@app.route("/user/<username>")

def user_comments(username):
	#displays an analysis of the last 50 comments by a user
	top, new, unique = comment_scraper.vocab_analysis(comment_scraper.get_user_comments(username),username)
	return "Top: " + repr(top) + "\n" + "Unique: " + repr(unique) + "\n" + "New: " + repr(new)