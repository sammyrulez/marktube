

def diigo_importer(diigo_user):
	username = settings.DIIGO_USER
	password = settings.DIIGO_PASSWORD
	
	key = settings.DIIGO_KEY
	action_url = "https://secure.diigo.com/api/v2/bookmarks?key=%s&user=%s" % (key,diigo_user)
	req = urllib2.Request(action_url)
	base64string = base64.encodestring('%s:%s' % (username, password))[:-1]
	authheader =  "Basic %s" % base64string
	req.add_header("Authorization", authheader)
	f = urllib2.urlopen(req)
	