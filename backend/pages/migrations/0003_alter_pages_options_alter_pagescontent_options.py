# Generated by Django 4.0.6 on 2022-07-15 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_pages_slug_pagescontent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pages',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='pagescontent',
            options={'ordering': ('name',)},
        ),
    ]
