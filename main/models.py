from django.db import models
from django import forms
from django.contrib.auth.models import User 
from datetime import datetime

#Locations
LOCATION_CHOICES  = (
      ('New York', 'New York'),
      ('San Francisco', 'San Francisco'),
      ('Washington DC', 'Washington DC'),
      ('hello', 'hello')
)

class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True)
	first_name = models.CharField(max_length=250, null=True, blank=True)
	last_name = models.CharField(max_length=250, null=True, blank=True)
	email = models.CharField(max_length=250, null=True, blank=True)
	birthday = models.DateField(blank=False, default=datetime.now)
	phone_number = models.CharField(max_length=15, null=True, blank=True)
	
	def __unicode__(self):
        	return self.user.username
	
	def get_absolute_url(self):
		return "/user/" % self.id

class EventDescription(models.Model):
	user = models.ForeignKey(UserProfile, blank=False)
	title = models.CharField(max_length=250, null=True, blank=False)
	address = models.CharField(max_length=250, null=True, blank=False)
	description = models.CharField(max_length=1000, null=True, blank=False)
	price = models.IntegerField(default=0)
	created_at = models.DateField(auto_now_add=True, blank=True)	
	
	class Meta:
        	ordering = ['-created_at']
	
	def __unicode__(self):
		return self.title

class EventImage(models.Model):
	event = models.ForeignKey(EventDescription, blank=False)
	image = models.ImageField(null=True, blank=True)
	
	def __unicode__(self):
		return self.id
		
class EventQuestion(models.Model):
	event = models.ForeignKey(EventDescription, blank=False)
	question = models.CharField(max_length=1000, null=True, blank=False)
	
	def __unicode__(self):
		return unicode(self.id)

class QuestionAnswer(models.Model):
	question = models.ForeignKey(EventQuestion, blank=False)
	user = models.ForeignKey(UserProfile, blank=False, null=True)
	answer = models.CharField(max_length=1000, null=True, blank=False)
	
	def __unicode__(self):
		return unicode(self.id)
				
class Event(models.Model):
	host = models.ForeignKey(UserProfile, blank=False, null=True)
	event = models.ForeignKey(EventDescription, blank=False)
	date = models.DateField(blank=False, default=datetime.now)
	time = models.TimeField(blank=False, auto_now_add=False, default=datetime.now) 
	available_slots = models.IntegerField(default=0)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	
	def __unicode__(self):
    		return unicode(self.id)

class Reservation(models.Model):
	Event = models.ForeignKey(Event)
	User = models.ForeignKey(UserProfile)

	def __unicode__(self):
		return self.id

