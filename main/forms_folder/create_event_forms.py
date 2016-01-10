from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from main.models import UserProfile, EventDescription, Event
from django.contrib.admin import widgets
from datetime import datetime
from functools import partial
import datetime


class CreateDescription(forms.Form):
        title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder': 'Quickly describe what you want to do', 'class': 'form-control'}))
	description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'placeholder': 'Talk about the activity, what will happen, and where', 'class': 'form-control'}))
       	
	class Meta:
                fields = ('title', 'description')

class AboutYou(forms.Form):
	about_you = forms.CharField(label='About You', widget=forms.Textarea(attrs={'placeholder': 'Tell us why you\'re qualified to run this activity', 'class': 'form-control'}))

	class Meta:
		fields = ('about_you')

class Location(forms.Form):
	address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'placeholder': 'Where are you hosting this?', 'class': 'form-control'}))
	
	class Meta:
		fields = ('address')

class Pricing(forms.Form):
	price  = forms.IntegerField(label='Price', widget=forms.TextInput(attrs={'placeholder': 'Enter a price', 'class': 'form-control'}))
	
	class Meta:
		fields = ('price')

