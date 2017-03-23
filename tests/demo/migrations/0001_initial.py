# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-26 06:08
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DemoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char', models.CharField(max_length=255, verbose_name='Ch\xe4\u0159')),
                ('integer', models.IntegerField()),
                ('logic', models.BooleanField(default=False)),
                ('null_logic', models.NullBooleanField(default=None)),
                ('date', models.DateField()),
                ('datetime', models.DateTimeField()),
                ('time', models.TimeField()),
                ('decimal', models.DecimalField(decimal_places=3, max_digits=10)),
                ('email', models.EmailField(max_length=254)),
                ('float', models.FloatField()),
                ('bigint', models.BigIntegerField()),
                ('generic_ip', models.GenericIPAddressField()),
                ('url', models.URLField()),
                ('text', models.TextField()),
                ('unique', models.CharField(max_length=255, unique=True)),
                ('nullable', models.CharField(max_length=255, null=True)),
                ('blank', models.CharField(blank=True, max_length=255, null=True)),
                ('not_editable', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('choices', models.IntegerField(choices=[(1, 'Choice 1'), (2, 'Choice 2'), (3, 'Choice 3')])),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DemoOneToOne',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('demo', models.OneToOneField(to='demo.DemoModel', related_name='onetoone')),
            ],
        ),
    ]
