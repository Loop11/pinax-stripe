# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-12-20 03:16
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_stripe', '0005_auto_20161006_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', models.CharField(max_length=191, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount_off', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('currency', models.CharField(default='usd', max_length=10)),
                ('duration', models.CharField(default='once', max_length=10)),
                ('duration_in_months', models.PositiveIntegerField(null=True)),
                ('livemode', models.BooleanField(default=False)),
                ('max_redemptions', models.PositiveIntegerField(null=True)),
                ('metadata', models.JSONField(null=True)),
                ('percent_off', models.PositiveIntegerField(null=True)),
                ('redeem_by', models.DateTimeField(null=True)),
                ('times_redeemed', models.PositiveIntegerField(null=True)),
                ('valid', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
