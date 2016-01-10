from django.conf.urls import patterns, url, include
from main import views
from django.forms.formsets import formset_factory

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^home/$', views.home, name='home'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^activities/$', views.activities, name='activities'),
	url(r'^schedule/$', views.schedule, name='schedule'),
	url(r'^create/$', views.create.as_view(), name='create'),
	url(r'^upload/image/$', views.image_upload, name='image_upload'),
	url(r'^schedule/date/(?P<event_id>\d+)/$', views.ContactWizard.as_view(views.FORMS), name='schedule_date'),
	url(r'^edit_event/(?P<id>\d+)/$', views.edit_event, name='edit_event'),
	url(r'^delete_event/(?P<id>\d+)/$', views.delete_event, name='delete_event'),
	url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.logout_user, name='logout'),
	url('', include('django.contrib.auth.urls', namespace='auth')),
	url('', include('social.apps.django_app.urls', namespace='social'))
)
