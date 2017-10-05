# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-10-05 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_fix-translation-model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=32, unique=True, verbose_name='Project feature tag')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
        ),
        migrations.AddField(
            model_name='feature',
            name='projects',
            field=models.ManyToManyField(blank=True, related_name='features', to='projects.Project'),
        ),
    ]