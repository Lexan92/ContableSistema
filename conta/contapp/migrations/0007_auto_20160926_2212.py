# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-27 04:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contapp', '0006_auto_20160926_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimiento',
            name='idCuenta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contapp.cuenta'),
        ),
    ]
