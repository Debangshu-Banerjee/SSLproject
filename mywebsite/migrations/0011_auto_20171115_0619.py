# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-15 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0010_auto_20171115_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='designation',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
