# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.ForeignKey(to='main.EventDescription'),
            preserve_default=True,
        ),
    ]
