# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-31 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20161101_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
