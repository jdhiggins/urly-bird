# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0004_auto_20150619_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='short',
            field=models.CharField(null=True, max_length=255),
        ),
    ]
