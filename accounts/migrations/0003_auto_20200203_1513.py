# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-03 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200203_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='img'),
        ),
    ]
