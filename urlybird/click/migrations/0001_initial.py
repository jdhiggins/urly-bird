# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('time', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('browser', models.CharField(max_length=500, null=True)),
                ('user', models.IntegerField(max_length=255, null=True)),
                ('bookmark', models.ForeignKey(to='bookmark.Bookmark')),
            ],
        ),
    ]
