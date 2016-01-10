# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20151016_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='creator',
        ),
    ]
