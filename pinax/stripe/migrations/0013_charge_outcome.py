# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 15:40
from __future__ import unicode_literals

from django.db import migrations, models



class Migration(migrations.Migration):

    dependencies = [
        ('pinax_stripe', '0014_blank_with_null'),
    ]

    operations = [
        migrations.AddField(
            model_name='charge',
            name='outcome',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
