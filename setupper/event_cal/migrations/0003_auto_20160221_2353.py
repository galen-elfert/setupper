# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 23:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_cal', '0002_building_name_short'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hex_value', models.CharField(max_length=6)),
            ],
        ),
        migrations.AddField(
            model_name='setup',
            name='pickup_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='setup',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setup',
            name='setup_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='colour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='event_cal.Colour'),
        ),
    ]
