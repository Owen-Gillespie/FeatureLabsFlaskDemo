from app import db, models

users = models.Username.query.all()
words = models.Word.query.all()
comments = models.Comment.query.all()

for user in users:
	db.session.delete(user)

for word in words:
	db.session.delete(word)

for comment in comments:
	db.session.delete(comment)
db.session.commit()