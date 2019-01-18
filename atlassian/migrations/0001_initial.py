# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-08 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityContext',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shared_secret', models.CharField(max_length=512)),
                ('key', models.CharField(max_length=512)),
                ('client_key', models.CharField(max_length=512)),
                ('host', models.CharField(max_length=512)),
            ],
        ),
    ]
