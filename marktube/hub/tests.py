from django.test import TestCase
from marktube.hub.management.commands.importer import Command
from django.contrib.auth.models import User


class CommandTest(TestCase):

	fixtures = ['users.json', 'tube.json']

	def test_import_bookmarks(self):
		c = Command()
		c.handle()
        
