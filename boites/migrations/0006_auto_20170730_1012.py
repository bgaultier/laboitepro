# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-30 08:12
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boites', '0005_auto_20170723_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tileapp',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name="Type d'app"),
        ),
        migrations.AlterField(
            model_name='tileapp',
            name='object_id',
            field=models.PositiveIntegerField(verbose_name="Identifiant de l'app"),
        ),
    ]
