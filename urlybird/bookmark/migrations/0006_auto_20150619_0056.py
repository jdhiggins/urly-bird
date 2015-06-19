# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0005_auto_20150619_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='short',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
    ]
