# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 03:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timezone', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter_id', models.CharField(blank=True, max_length=25, null=True)),
                ('twitter_access_token', models.CharField(blank=True, max_length=75, null=True)),
                ('twitter_access_token_secret', models.CharField(blank=True, max_length=75, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
