from django.db import models
from django.contrib.auth.models import User

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
	
