# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-12-12 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0006_sphere_sphere_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='mem',
            name='Picture',
            field=models.CharField(default='https://media.thequestion.ru/image/with_proportions/744x0/1e134189fec3995caf26825101b19ae4632848ca?url=https%3A%2F%2Fthequestion.s3.eu-central-1.amazonaws.com%2F652%2F316357-925ac9e9.jpeg', max_length=500),
            preserve_default=False,
        ),
    ]
