from app import db

class Word(db.Model):
	__tablename__ = 'words'
	word = db.Column(db.String(20), primary_key=True)
	totalUse = db.Column(db.Integer,index=True)

	def __repr__(self):
		return '<Word: %(wordname)r Uses: %(wordcount)i>' % {"wordname": self.word, "wordcount":self.totalUse}

class Username(db.Model):
	__tablename__ = 'usernames'
	Username = db.Column(db.String(50), primary_key=True)

	def __repr__(self):
		return '<Username:%r>' % self.Username

class Comment(db.Model):
	__tablename__ = 'comments'
	comment = db.Column(db.String(20), primary_key=True)

	def __repr__(self):
		return '<comment %i>' % self.Comment