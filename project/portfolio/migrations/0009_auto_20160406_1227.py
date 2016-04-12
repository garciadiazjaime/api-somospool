# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-06 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20160405_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='block',
            name='type',
            field=models.CharField(choices=[('IMAGE', 'IMAGE'), ('DESCRIPTION', 'DESCRIPTION')], default='IMAGE', max_length=20),
        ),
    ]
