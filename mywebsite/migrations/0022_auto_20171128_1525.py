# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-28 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0021_merge_20171118_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='room',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='designation',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='research',
            name='research_interest_description',
            field=models.TextField(blank=True, max_length=1500),
        ),
        migrations.AlterField(
            model_name='research',
            name='research_interest_title',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
