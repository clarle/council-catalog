# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-29 23:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('djangohaystack', '0009_auto_20170628_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='file_upload',
            field=models.FileField(default=django.utils.timezone.now, upload_to='fileup'),
            preserve_default=False,
        ),
    ]