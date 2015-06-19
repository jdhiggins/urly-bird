# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='description',
            field=models.CharField(max_length=255, default=None),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='title',
            field=models.CharField(max_length=255, default=None),
        ),
    ]
