# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0018_auto_20150813_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('available_slots', models.IntegerField(default=0)),
                ('creator', models.ForeignKey(related_name='event_requests_created', to=settings.AUTH_USER_MODEL)),
                ('description', models.OneToOneField(to='main.EventDescription')),
                ('users', models.ManyToManyField(to='main.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
