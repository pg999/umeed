# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 09:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=40, null=True)),
                ('company_address', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(blank=True, max_length=40, null=True)),
                ('employee_count', models.CharField(blank=True, max_length=40, null=True)),
                ('company_introduction', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('date_of_posting', models.DateField(auto_now_add=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('vacancies', models.IntegerField(blank=True, null=True)),
                ('last_date', models.DateField(blank=True, max_length=30, null=True)),
                ('company_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='industry.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Job_skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('job_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='industry.Job')),
            ],
        ),
    ]