# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_event_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventdescription',
            old_name='cost',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='eventdescription',
            name='slots',
        ),
    ]
