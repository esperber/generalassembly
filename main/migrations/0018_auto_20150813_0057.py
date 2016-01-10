# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20150812_0039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventdescription',
            old_name='location',
            new_name='address',
        ),
    ]
