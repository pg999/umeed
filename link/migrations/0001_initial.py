# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('founder', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('detail', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_name', models.CharField(blank=True, max_length=200, null=True)),
                ('module_description', models.CharField(blank=True, max_length=700, null=True)),
                ('video_path', models.CharField(blank=True, max_length=200, null=True)),
                ('main_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='link.Course')),
            ],
        ),
    ]