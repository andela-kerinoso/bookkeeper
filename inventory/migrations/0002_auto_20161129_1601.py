# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('authors', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Category')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together=set([('title', 'authors')]),
        ),
    ]
