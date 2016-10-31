# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 05:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RideSystem_app', '0002_auto_20161031_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_id', models.IntegerField(blank=True, null=True)),
                ('driver_id', models.IntegerField(blank=True, null=True)),
                ('request_id', models.CharField(blank=True, max_length=20, null=True)),
                ('lat_from', models.CharField(blank=True, max_length=20, null=True)),
                ('long_from', models.CharField(blank=True, max_length=20, null=True)),
                ('lat_to', models.CharField(blank=True, max_length=20, null=True)),
                ('long_to', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='driver',
            name='lat',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='long',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='lat',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='long',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
