# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 10:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disputes', '0004_auto_20160806_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispute',
            name='text',
        ),
        migrations.AddField(
            model_name='dispute',
            name='state',
            field=models.IntegerField(choices=[(1, 'draft'), (2, 'open'), (3, 'finalised'), (4, 'assigned'), (5, 'proposed'), (6, 'resolved')], default=1),
        ),
        migrations.AlterField(
            model_name='dispute',
            name='customer2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dispute_customer2', to='users.Customer'),
        ),
    ]