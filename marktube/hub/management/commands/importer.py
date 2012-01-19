from marktube.tube.models import Bookmark

logger = logging.getLogger(__name__)

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
		data = f.read()

class Command(BaseCommand):
    help = 'Syncs user bookmarks'

    def handle(self, *args, **options):
        for user in User.objects.all():
            try:
               self.import_bookmarks(user)
            except Exception:
                raise CommandError('Error importing bookmarks')

	def import_bookmarks(self,user):
		for account in user.get_profile().accounts:
			logger.info("Importing %s for %s" % (account.name , user.username) )
			importer[account.name].import_data(user)
			
			

	def create_bookmarks(self,user, data,origin):
		for d in data:
			b = Bookmark() #TODO check if exist
			b.name = d['name']
			b.description = d['description']
			b.url = d['url']
			b.date = d['date']
			b.owner = user
			b.origin = origin
			b.save()

		

	
	
	
	