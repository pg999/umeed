# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aspirant_skill',
            name='percentage',
            field=models.FloatField(default=0.0, max_length=5, null=True),
        ),
    ]
