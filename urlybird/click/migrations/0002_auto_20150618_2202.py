# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('click', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='click',
            name='address',
            field=models.CharField(max_length=500, default=None),
        ),
        migrations.AlterField(
            model_name='click',
            name='browser',
            field=models.CharField(max_length=500, default=None),
        ),
        migrations.AlterField(
            model_name='click',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='click',
            name='user',
            field=models.IntegerField(default=None),
        ),
    ]
