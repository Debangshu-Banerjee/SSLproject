# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-10 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0004_auto_20171109_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='publications',
            field=models.TextField(blank=True, max_length=1500),
        ),
        migrations.AddField(
            model_name='profile',
            name='research_interest',
            field=models.TextField(blank=True, max_length=1500),
        ),
    ]
