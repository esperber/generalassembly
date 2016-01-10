# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_eventdescription_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventdescription',
            options={'ordering': ['created_at']},
        ),
    ]
