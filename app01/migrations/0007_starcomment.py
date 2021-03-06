# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-08-14 12:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app01', '0006_auto_20190813_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='StarComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.CharField(max_length=20, verbose_name='电影id')),
                ('star', models.CharField(max_length=10, verbose_name='星级评分')),
                ('status', models.BooleanField(default=True, verbose_name='评分状态')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='star_collect', to=settings.AUTH_USER_MODEL, verbose_name='评分人')),
            ],
            options={
                'verbose_name': '星级评分',
                'verbose_name_plural': '星级评分',
            },
        ),
    ]
