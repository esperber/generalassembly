# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_remove_event_creator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='description',
            new_name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='host',
            field=models.ForeignKey(to='main.UserProfile', null=True),
            preserve_default=True,
        ),
    ]
