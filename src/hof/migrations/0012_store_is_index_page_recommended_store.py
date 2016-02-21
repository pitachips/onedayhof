# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 12:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hof', '0011_auto_20160221_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='is_index_page_recommended_store',
            field=models.PositiveSmallIntegerField(blank=True, null=True, unique=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)]),
        ),
    ]
