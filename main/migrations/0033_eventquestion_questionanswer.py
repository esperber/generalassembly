# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20151219_0401'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=1000, null=True)),
                ('event', models.ForeignKey(to='main.EventDescription')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.CharField(max_length=1000, null=True)),
                ('question', models.ForeignKey(to='main.EventQuestion')),
                ('user', models.ForeignKey(to='main.UserProfile', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
