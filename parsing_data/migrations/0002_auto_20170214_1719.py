# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsing_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='targetplace',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
