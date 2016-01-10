from django.views.generic import View
from datetime import datetime
from django.shortcuts import render,render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from django.forms import formset_factory
from django.forms.models import modelformset_factory, inlineformset_factory 

from django.core.urlresolvers import reverse
from django.contrib.formtools.wizard.views import SessionWizardView

from main.forms import EventImageForm, PickEventForm, ScheduleConfirmation, ScheduleDate, QuestionForm, Answer, \
	 UserForm, EditUserProfileForm, UserProfileForm, LoginForm, CreateEventForm 

from .models import UserProfile, EventDescription, Event, EventQuestion
from main.forms_folder import create_event_forms


FORMS =[('0', ScheduleDate),
	('1', formset_factory(PickEventForm))]

TEMPLATES = {'0': 'main/schedule_date.html',
	     '1': 'main/schedule_time.html'}

FORMS_CREATE = [('0', create_event_forms.CreateDescription),
		('1', create_event_forms.AboutYou)]

TEMPLATES_CREATE = {'0': 'main/create_event_form/description.html',
		    '1': 'main/create_event_form/description.html'}

class ContactWizard(SessionWizardView):
	def get_template_names(self):
		return [TEMPLATES[self.steps.current]]
	
	def dispatch(self, request, *args, **kwargs):
    		self.event_id = kwargs.get('event_id', None)
		event = get_object_or_404(EventDescription, pk=self.event_id)

		if str(event.user)!=str(request.user.email):
			raise Http404

    		return super(ContactWizard, self).dispatch(request, *args, **kwargs)

	def get_form(self, step=None, data=None, files=None):
		form = super(ContactWizard, self).get_form(step, data, files)
		initial_data = []
		
		if step is None:
			step = self.steps.current
		
		if step == '1':
			date_list = self.get_cleaned_data_for_step('0')['date'].split(',')
			for date in date_list:
				formatted_date = datetime.strptime(date, '%Y-%m-%d')
				initial_data.append({'date':formatted_date.date()})
			
			form_holder = formset_factory(PickEventForm, extra=len(date_list), max_num=len(date_list))
			form = form_holder(data=data, initial=initial_data)

		return form


	def done(self, form_list, **kwargs):
		event_description = EventDescription.objects.get(id=self.event_id)
                profile = UserProfile.objects.get(email=self.request.user.email)	
		second_part = self.get_cleaned_data_for_step('1')
	
		for form_instance in second_part:
                	form = PickEventForm()
			event = form.save(commit=False)
			event.price = event_description.cost
			event.host = profile
			event.event = event_description
			event.date  = form_instance['date']
			event.time  = form_instance['time']
			event.available_slots = form_instance['available_slots']
			event.save()
		return HttpResponseRedirect('main/home.html')


def index(request):
	return render(request, 'main/index.html')

class create(View):
	main = CreateEventForm(prefix="main")
	question_formset = formset_factory(QuestionForm)
	template_name = 'main/create_event_form/create_body.html'
	
	def get(self, request, *args, **kwargs):
		form = self.main
		question_form = self.question_formset(prefix='question')
	
		return render(request, self.template_name, {'form':form, 'question':question_form })
		
	def post(self, request, *args, **kwargs):
		print request.FILES
		profile = UserProfile.objects.get(email=request.user.email)
		form = CreateEventForm(data=request.POST, prefix='main')
		question_form = self.question_formset(data=request.POST, prefix='question')
		
		if form.is_valid() and question_form.is_valid():
			event = form.save(commit=False)
			event.user = profile
			event.save()
			
			for question in question_form:
				q = question.save(commit=False)
				q.event = event
				q.save()

			return HttpResponseRedirect('main/home')
			
		return render(request, self.template_name , {'form': form, 'question': question_form})


def image_upload(request):
	print request.FILES

	return render(request, 'main/index.html')
	
		
def home(request):
	print request.FILES
	profile = UserProfile.objects.get(email=request.user.email)
	events = EventDescription.objects.all()
	return render(request , 'main/home.html', {'event': events, 'user':request.user})

def register(request):
	registered = False
	if request.method == 'POST':
         	user_form = UserForm(data=request.POST)
        	profile_form = UserProfileForm(data=request.POST)
        	if user_form.is_valid() and profile_form.is_valid():
            		user = user_form.save()
			user.username = user.email
            		user.set_password(user.password)
            		user.save()

            		# Since we need to set the user attribute ourselves, we set commit=False.
            		# This delays saving the model until we're ready to avoid integrity problems.
            		profile = profile_form.save(commit=False)
            		profile.user = user
			profile.email = user.email
			profile.first_name = user.first_name
			profile.last_name = user.last_name
            		profile.save()
            		registered = True
              	else:
			print user_form.errors, profile_form.errors

    	# Not a HTTP POST, so we render our form using two ModelForm instances.
    	else:
        	user_form = UserForm()
        	profile_form = UserProfileForm()
		
	return render(request,
      	    'main/home.html',
            {'user_form': user_form, 'profile_form': profile_form} )

def profile(request):
	profile = UserProfile.objects.get(email=request.user.email)
	form = EditUserProfileForm(request.POST or None,instance=profile)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
	context= RequestContext(request, 
			{'request': request,
			 'profile': profile,
			 'form':form,
			 'user': request.user
			})
	
	return render_to_response('main/profile.html', context)
'''
def create(request):
	profile = UserProfile.objects.get(email=request.user.email)
        if request.method == 'POST':
		form = CreateEventForm(data=request.POST)
                if form.is_valid():
			event = form.save(commit=False)
			event.user = profile
			event.save()
	else:
		form = CreateEventForm()

        context= RequestContext(request,
                        {'request': request,
			 'profile': profile,
                         'form':form,
                         'user': request.user
                        })

        return render_to_response('main/create.html', context)
'''

def edit_event(request,id):
	event = get_object_or_404(EventDescription, pk=id)
	form = CreateEventForm(data=request.POST or None,instance=event)
        if request.method == 'POST':
                if form.is_valid():
                	form.save()
			return HttpResponseRedirect(reverse('activities'))

        context= RequestContext(request,
                        {'request': request,
                         'form':form
                        })
        return render_to_response('main/edit.html', context)

#Delete Event Description Method, deletes the event description template
def delete_event(request, id):
	event = get_object_or_404(EventDescription, pk=id).delete()
	return HttpResponseRedirect(reverse('activities'))

#Activities Method, CRUD Listing of activities
def activities(request):
	profile = UserProfile.objects.get(email=request.user.email)
	events = EventDescription.objects.filter(user = profile)
	context = RequestContext(request, 
			{'request': request,
			 'events': events,
			 'profile': profile
			})
	return render_to_response('main/activities.html', context)

#Schedule Method, User can select existing event or create a new one
def schedule(request):
        profile = UserProfile.objects.get(email=request.user.email)
        events = EventDescription.objects.filter(user = profile)
	
        context = RequestContext(request, 
                        {'request': request,
                         'events': events,
                         'profile': profile
                        })
        return render_to_response('main/schedule.html', context)

#Login Method
def user_login(request):
	form = LoginForm(request.POST or None)
    	if request.POST and form.is_valid():
        	user = form.login(request)
        	if user:
            		login(request, user)
            		return HttpResponseRedirect('/main/home')# Redirect to a success page.
	return render(request, 'main/index.html', {'form': form })

#Logout Method
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/main/')
