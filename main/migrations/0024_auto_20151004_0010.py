# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20150824_2326'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventdescription',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.DecimalField(default=0, max_digits=2, decimal_places=2),
            preserve_default=True,
        ),
    ]
