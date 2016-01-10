# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_eventdescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdescription',
            name='description',
            field=models.CharField(max_length=1000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventdescription',
            name='location',
            field=models.CharField(max_length=250, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventdescription',
            name='title',
            field=models.CharField(max_length=250, null=True),
            preserve_default=True,
        ),
    ]
