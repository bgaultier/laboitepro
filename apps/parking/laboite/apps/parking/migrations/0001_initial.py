# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-26 10:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boites', '0002_auto_20161224_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppParking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de cr\xe9ation')),
                ('enabled', models.BooleanField(default=True, help_text='Indique si cette app est activ\xe9e sur votre bo\xeete', verbose_name='App activ\xe9e ?')),
                ('last_activity', models.DateTimeField(null=True, verbose_name='Derni\xe8re activit\xe9')),
                ('parking', models.CharField(choices=[('HFR', 'Henri Fr\xe9ville'), ('JFK', 'J.F. Kennedy'), ('POT', 'La Poterie'), ('PRE', 'Les Pr\xe9ales'), ('VU', 'Villejean-Universit\xe9')], help_text="Veuillez saisir l'identifiant Timeo de votre arr\xeat de bus", max_length=3)),
                ('open', models.NullBooleanField(default=None, verbose_name='Parking ouvert ?')),
                ('available', models.PositiveSmallIntegerField(default=None, null=True, verbose_name='Places disponibles')),
                ('occupied', models.PositiveSmallIntegerField(default=None, null=True, verbose_name='Places occup\xe9es')),
                ('boite', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='boites.Boite', verbose_name='Bo\xeete')),
            ],
            options={
                'verbose_name': 'Configuration : Parking',
                'verbose_name_plural': 'Configurations : Parking',
            },
        ),
    ]