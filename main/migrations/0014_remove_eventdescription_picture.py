# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20150811_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventdescription',
            name='picture',
        ),
    ]
