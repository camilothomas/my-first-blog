# add bits from other files
from django.db import models
from django.utils import timezone

# defines our model - it is an object
# class is a special keyword that indicates that we are defining an object
# Post is the name of our model (always start a class name with an uppercase letter.)
# models.Model means that Post is a Django Model, so Django knows that it should be saved in the database

class Post(models.Model):
# define type of each field (text, number, date, a relation to another object like a user)


	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

# this is the publish method
			
	def publish(self):
		self.published_date = timezone.now()
		self.save()
# __ aka dunder		
	def __str__(self):
		return self.title 