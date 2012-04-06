from marktube.tube.models import BookmarkUrl
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
import logging
import urllib2
import base64
import json
from datetime import  datetime
from django.conf import settings

logger = logging.getLogger('tube-console')

def diigo_importer(diigo_user,user):
		username = settings.DIIGO_USER
		password = settings.DIIGO_PASSWORD
		key = settings.DIIGO_KEY
		
		action_url = "https://secure.diigo.com/api/v2/bookmarks?key=%s&user=%s" % (key,diigo_user)
		logger.debug(action_url)
		req = urllib2.Request(action_url)
		base64string = base64.encodestring('%s:%s' % (username, password))[:-1]
		authheader =  "Basic %s" % base64string
		req.add_header("Authorization", authheader)
		f = urllib2.urlopen(req)
		data = f.read()
		logger.debug(data)
		json_data = json.loads(data)
		lx = []
		for j in json_data:
			lx.append({'name':j['title'] , 'description' : j['desc'] , 'url' : j['url'] ,'date' :  datetime.strptime(j['created_at'],'%Y/%m/%d %H:%M:%S +%f') })
		
		return lx
		
def pinboard_importer(pinboard_user,user):
	pass

def delicious_importer(delicious_user,user):
	pass
			
		

class Command(BaseCommand):
	
	help = 'Syncs user bookmarks'
	
	importers = {'DIIGO':diigo_importer ,}
	
	

	def import_bookmarks(self,user):
		try:
			if user.get_profile():
				for account in user.get_profile().tpaccount_set.all():
					logger.info("Importing %s for %s" % (account.service , user.username) )
					bookmarks = self.importers[account.service](account.tp_username,user)
					logger.debug(bookmarks)
					self.create_bookmarks(user,bookmarks,account.service)
		except Exception as detail:
			logger.error("Failed Importing  for %s because %s" % ( user.username , str(detail)) )
		
				
			

	def create_bookmarks(self,user, data,origin):
		for d in data:
			b = BookmarkUrl() #TODO check if exist
			b.name = d['name']
			b.description = d['description']
			b.url = d['url']
			b.date = d['date']
			b.owner = user
			b.origin = origin
			b.save()

	def handle(self, *args, **options):
		for user in User.objects.all():
			try:
				self.import_bookmarks(user)
			except Exception  as detail:
				raise CommandError("Error importing bookmarks : %s" % str(detail) )

	

		

	
	
	
	