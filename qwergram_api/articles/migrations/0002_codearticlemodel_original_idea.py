# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 03:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='codearticlemodel',
            name='original_idea',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.PotentialIdeaModel'),
        ),
    ]