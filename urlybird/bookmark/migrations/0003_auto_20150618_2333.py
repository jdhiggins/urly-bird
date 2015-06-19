# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0002_auto_20150618_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='edited',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='short',
            field=models.URLField(null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
