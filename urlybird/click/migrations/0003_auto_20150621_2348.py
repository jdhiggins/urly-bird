# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('click', '0002_auto_20150618_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='click',
            name='user',
            field=models.IntegerField(null=True, default=None),
        ),
    ]
