# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-02-14 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataplot', '0003_auto_20170214_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='chartdata',
            name='sector',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='chartdata',
            name='ticker',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]