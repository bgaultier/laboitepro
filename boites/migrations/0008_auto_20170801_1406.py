# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-01 12:06
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boites', '0007_auto_20170801_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tile',
            name='duration',
            field=models.PositiveSmallIntegerField(default=5, help_text='Veuillez saisir une dur\xe9e durant laquelle la tuile sera affich\xe9e (en secondes)', verbose_name="Dur\xe9e d'affichage de la tuile"),
        ),
    ]
