from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.core import validators
from django.contrib.auth.models import User
from main.models import UserProfile, EventDescription, Event, \
	EventQuestion, QuestionAnswer, EventImage
from django.contrib.admin import widgets 
from datetime import datetime
from functools import partial
import datetime


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    birthday = forms.DateField(widget=forms.DateInput(format = '%m/%d/%Y'))
    
    class Meta:
        model = UserProfile
        fields= ('birthday',)

class EditUserProfileForm(forms.ModelForm):
	first_name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))
	birthday = forms.DateTimeField(input_formats=('%m/%d/%Y',),widget=forms.TextInput(attrs={'class': 'form-control'}))
	phone_number  = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class': 'form-control'}))
	
	class Meta:
        	model = UserProfile
        	fields= ('email','first_name', 'last_name', 'birthday', 'phone_number')

class CreateEventForm(forms.ModelForm):
    title = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))
    address  = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(max_length=2,widget=forms.TextInput(attrs={'class': 'form-control'}))
    zip_code = forms.CharField(max_length=6,widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'class': 'form-control description-input'}))
    price = forms.IntegerField(validators=[validators.validate_integer], widget=forms.TextInput(attrs={'class': 'form-control'}))
        
        
    class Meta:
    	model = EventDescription
        exclude= ('user',)

class EventImageForm(forms.ModelForm):
	image = forms.ImageField()
	
	class Meta:
		model=EventImage
		exclude = ('event',)
		
class QuestionForm(forms.ModelForm):
	question = forms.CharField(max_length=255, label='', widget=forms.TextInput(attrs={'class': 'form-control questionaire-input'}))
		
	class Meta:
		model = EventQuestion
		fields = ('question',)
				
class Answer(forms.ModelForm):
	answer = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = QuestionAnswer
		exclude = ('question', 'user')
				
class PickEventForm(forms.ModelForm):
	time = forms.TimeField(label='Time', widget=forms.TextInput(attrs={'class': 'form-control time_entry_field'}))
	available_slots = forms.IntegerField(label='Slots', widget=forms.TextInput(attrs={'class': 'form-control slot_field'}))
	date = forms.DateField(label='', widget=forms.HiddenInput(attrs={'class': 'date-input'}))
	
	class Meta:
		model = Event
		fields = ('time', 'available_slots', 'date')
		exclude = ('host', 'event')
			
class ScheduleDate(forms.Form):
	date = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'date-input'}))

class ScheduleConfirmation(forms.Form):
	confirmation = forms.CharField()
