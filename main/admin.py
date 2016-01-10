from django.contrib import admin
from main.models import UserProfile, EventDescription, Event, EventQuestion, QuestionAnswer

admin.site.register(UserProfile)
admin.site.register(EventDescription)
admin.site.register(Event)
admin.site.register(EventQuestion)
# Register your models here.
