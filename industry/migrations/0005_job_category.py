# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industry', '0004_auto_20170327_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
