# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-08 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrasion', '0015_auto_20160408_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='access_code',
            field=models.CharField(db_index=True, max_length=6, unique=True),
        ),
    ]
