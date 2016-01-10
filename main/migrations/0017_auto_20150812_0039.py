# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20150811_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdescription',
            name='user',
            field=models.OneToOneField(to='main.UserProfile'),
            preserve_default=True,
        ),
    ]
