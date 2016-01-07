import praw,string, operator
user_agent = "FeatureLab Demo Scraper"
r = praw.Reddit(user_agent = user_agent)
request_limit=500


def get_user_comments(user_name):
	user = r.get_redditor(user_name)
	comments=user.get_comments(limit=request_limit)
	print user_name
	return list(comments)

def vocab_analysis(comments):
	vocab={}
	i=0
	for comment in comments:
		text = comment.body
		noPunctText=translate_non_alphanumerics(text)
		words=noPunctText.encode('ascii','ignore').lower().split()
		for word in words:
			if len(word)<20 and len(word)>3:
				vocab[word]= (vocab.get(word,0)+1)
	print len(vocab)
	print 
	return dict(sorted(vocab.iteritems(), key=operator.itemgetter(1), reverse=True)[:10])

def translate_non_alphanumerics(to_translate, translate_to=u''):
    not_letters_or_digits = u'!"#%\'()*+,-./:;<=>?@[\]^_`{|}~'
    translate_table = dict((ord(char), translate_to) for char in not_letters_or_digits)
    return to_translate.translate(translate_table)