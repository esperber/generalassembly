# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_userprofile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(default=2, max_length=25, choices=[(b'New York', b'New York'), (b'San Francisco', b'San Francisco'), (b'Washington DC', b'Washington DC')]),
            preserve_default=False,
        ),
    ]
