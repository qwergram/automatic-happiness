# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 18:38
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20160525_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statmodel',
            name='value',
            field=jsonfield.fields.JSONField(),
        ),
    ]
