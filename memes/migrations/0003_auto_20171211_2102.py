# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-12-11 21:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0002_creator_source_mem_tag_sphere_mem_sphere_source_sphere_tag_user_likes_mem_user_source_user_tag_user_'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Memes',
            new_name='Mem',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
