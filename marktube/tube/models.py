from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	extradata = models.TextField(blank=True , null=True)
	
	def __unicode__(self):
		return "UserProfile for %s" % self.user.username

class TPAccount(models.Model):
	owner = models.ForeignKey(UserProfile)
	service = models.CharField(max_length=255)
	tp_username = models.CharField(max_length=255)
	extradata = models.TextField(blank=True , null=True)
	
	def __unicode__(self):
		return "%s for %s" % (self.service,self.owner.user.username)
		
	class Meta():
		verbose_name = "Third Party Account"
	

class Bookmark(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True , null=True)
	url = models.URLField()
	date = models.DateField()
	created_at = models.DateTimeField(auto_now=True, auto_now_add=True)
	owner = models.ForeignKey(User)
	origin = models.CharField(max_length=255)
	
class Channel(models.Model):
	name = models.CharField(max_length=255)
	is_private = models.BooleanField(default=False)
	followers = models.ManyToManyField(User)
	bookmarks =  models.ManyToManyField(Bookmark)
	
