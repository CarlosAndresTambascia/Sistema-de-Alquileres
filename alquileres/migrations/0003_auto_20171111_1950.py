# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-11 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alquileres', '0002_auto_20171111_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='nombre',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]