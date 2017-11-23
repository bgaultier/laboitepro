# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboite.apps.wifi', '0002_auto_20170310_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appwifi',
            name='preshared_key',
            field=models.CharField(help_text='Veuillez indiquer la cl\xe9 de protection de votre r\xe9seau', max_length=128, verbose_name='Cl\xe9 de protection'),
        ),
        migrations.AlterField(
            model_name='appwifi',
            name='ssid',
            field=models.CharField(help_text='Veuillez indiquer le nom de votre r\xe9seau wifi', max_length=64, verbose_name='Nom du r\xe9seau'),
        ),
    ]