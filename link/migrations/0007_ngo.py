# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0006_course_online'),
    ]

    operations = [
        migrations.CreateModel(
            name='NGO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(blank=True, max_length=40, null=True)),
                ('password', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
