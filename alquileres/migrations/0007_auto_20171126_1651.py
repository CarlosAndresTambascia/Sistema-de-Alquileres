# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 19:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alquileres', '0006_auto_20171117_1949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudad',
            options={'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='fechaalquiler',
            options={'verbose_name_plural': 'FechasAlquiler'},
        ),
        migrations.AlterModelOptions(
            name='propiedad',
            options={'verbose_name_plural': 'Propiedades'},
        ),
        migrations.RemoveField(
            model_name='propiedad',
            name='numeroFicha',
        ),
        migrations.RemoveField(
            model_name='propiedad',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='huesped',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='numeroReserva',
        ),
        migrations.AddField(
            model_name='reserva',
            name='apellido',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='propiedad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='alquileres.Propiedad'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fechaReserva',
            field=models.DateField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='Huesped',
        ),
    ]
