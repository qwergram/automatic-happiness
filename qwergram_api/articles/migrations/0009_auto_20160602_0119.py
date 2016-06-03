# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20160525_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalStockModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('open', models.FloatField()),
                ('close', models.FloatField()),
                ('volume', models.IntegerField()),
                ('adj_close', models.FloatField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='historicalstockmodel',
            unique_together=set([('symbol', 'date')]),
        ),
    ]