# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_userprofile_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventDescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, null=True, blank=True)),
                ('description', models.CharField(max_length=1000, null=True, blank=True)),
                ('picture', models.ImageField(upload_to=b'path/', verbose_name=b'Label')),
                ('cost', models.IntegerField(default=0)),
                ('slots', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=250, null=True, blank=True)),
                ('user', models.OneToOneField(to='main.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
