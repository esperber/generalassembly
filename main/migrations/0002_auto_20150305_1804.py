# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='date',
            new_name='birthday',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.TextField(default=b'herro'),
            preserve_default=True,
        ),
    ]
