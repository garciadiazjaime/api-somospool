# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-24 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_block_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
