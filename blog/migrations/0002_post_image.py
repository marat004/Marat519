# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-18 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to=None),
            preserve_default=False,
        ),
    ]
