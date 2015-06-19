# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0003_auto_20150618_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='short',
            field=models.URLField(default=None, max_length=255),
        ),
    ]
