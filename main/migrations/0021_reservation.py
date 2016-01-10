# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20150816_0329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Event', models.ForeignKey(to='main.Event')),
                ('User', models.ForeignKey(to='main.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
