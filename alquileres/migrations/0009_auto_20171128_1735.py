# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alquileres', '0008_auto_20171126_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='total',
            field=models.IntegerField(),
        ),
    ]