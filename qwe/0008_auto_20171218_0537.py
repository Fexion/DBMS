# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-12-18 05:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0007_mem_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sphere',
            name='Sphere_Theme',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='memes.Sphere'),
        ),
    ]
