# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterModelOptions(
            name='usertype',
            options={},
        ),
        migrations.AlterField(
            model_name='services',
            name='is_active',
            field=models.CharField(default=1, max_length=1),
        ),
    ]
