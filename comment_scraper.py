import praw,string, operator
from app import db, models
user_agent = "FeatureLab Demo Scraper"
r = praw.Reddit(user_agent = user_agent)
request_limit=1000
debug=False

def get_user_comments(username):
	user = r.get_redditor(username)
	comments=user.get_comments(limit=request_limit)
	return list(comments)

def vocab_analysis(comments, username):
	vocab={}
	newWords=[]
	uniqueWords=[]
	commentWords={}
	databaseWords=(db.session.execute("SELECT SUM(totalUse) AS wordSum FROM words").first()).wordSum
	if databaseWords is None:
		databaseWords=0
	newUser=True
	if models.Username.query.get(username) is not None:
		newUser=False
		if debug: print "old user"
	else:
		if debug: print "new user"
		Username = models.Username(Username=username)
		db.session.add(Username)
	
	for comment in comments:
		commentID=comment.id.encode('ascii','ignore')
		if debug: print "commentID: " + commentID
		text = comment.body
		if debug: print "Text: " + repr(text)
		noPunctText=translate_non_alphanumerics(text)
		words=noPunctText.encode('ascii','ignore').lower().split()
		if models.Comment.query.get(commentID) is None:
			'''processes all the words from new comments, new words are added to the list'''
			if debug: print "New comment"
			for word in words:
				if len(word)<20:
					if debug: print "added " + word + " to new comments words"
					commentWords[word] = commentWords.get(word,0) + 1
			db.session.add(models.Comment(comment=commentID))
		else:
			if debug: print "Old comment"
			for word in words:
				'''puts all appropriate words into the vocab dict'''
				if len(word)<20:   
					'''Consider parsing for links etc'''
					if debug: print "added " + word + " to vocab list"
					vocab[word] = vocab.get(word,0) + 1
					
	for word in commentWords:
		if db.session.query(models.Word).filter(models.Word.word==word).count()==0:
			if debug: print "new word: " + word + "!"
			newWordEntry = models.Word(word=word, totalUse=commentWords[word])
			db.session.add(newWordEntry)
			newWords.append(word)
		else:
			if debug: print "old word: " + word
			vocab[word] = vocab.get(word,0) +1
			db.session.query(models.Word).filter(models.Word.word==word).update({models.Word.totalUse: models.Word.totalUse+1})
	for word in vocab:
		otherUses=(models.Word.query.get(word).totalUse)
		if otherUses==vocab[word]:
			uniqueWords.append(word)
		else:
			vocab[word] =  float(vocab[word]) / float(otherUses)
	for word in uniqueWords:
		del vocab[word]				
	db.session.commit()
	if debug: print "newWords: " + str(newWords)
	if debug: print vocab
	return dict(sorted(vocab.iteritems(), key=operator.itemgetter(1), reverse=True)[:20]), newWords, uniqueWords

def translate_non_alphanumerics(to_translate, translate_to=u''):
    not_letters_or_digits = u'!"#%\'()*+,-./:;<=>?@[\]^_`{|}~0123456789$&'
    translate_table = dict((ord(char), translate_to) for char in not_letters_or_digits)
    return to_translate.translate(translate_table)