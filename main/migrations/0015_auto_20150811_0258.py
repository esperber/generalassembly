# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_eventdescription_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdescription',
            name='user',
            field=models.OneToOneField(blank=True, to='main.UserProfile'),
            preserve_default=True,
        ),
    ]
