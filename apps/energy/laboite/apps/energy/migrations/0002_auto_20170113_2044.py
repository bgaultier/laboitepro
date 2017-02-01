# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-13 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboite.apps.energy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appenergy',
            name='last_activity',
            field=models.DateTimeField(null=True, verbose_name='Derni\xe8re activit\xe9'),
        ),
        migrations.AlterField(
            model_name='appenergy',
            name='url',
            field=models.URLField(default='https://emoncms.org/', help_text="Veuillez indiquer l'adresse de votre serveur emoncms", verbose_name='URL du serveur emoncms'),
        ),
    ]
