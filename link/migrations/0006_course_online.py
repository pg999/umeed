# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0005_auto_20170331_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='online',
            field=models.BooleanField(default=True),
        ),
    ]
