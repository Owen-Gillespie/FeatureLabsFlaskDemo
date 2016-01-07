from app import db

class Word(db.Model):
	word = db.Column(db.String(20), primary_key=True)
	totalUse = db.Column(db.Integer,index=True)

	def __repr__(self):
		return '<Word: %(wordname)r Uses: %(wordcount)i>' % {"wordname": self.word, "wordcount":self.totalUse}