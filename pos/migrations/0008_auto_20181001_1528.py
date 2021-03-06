# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-01 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0007_user_is_crew'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='credit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='crew',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
