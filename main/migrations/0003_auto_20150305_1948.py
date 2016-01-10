# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150305_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='location',
            field=models.CharField(max_length=25, choices=[(b'New York', b'New York'), (b'San Francisco', b'San Francisco'), (b'Washington DC', b'Washington DC')]),
            preserve_default=True,
        ),
    ]
