# Generated by Django 5.0.6 on 2024-05-23 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagament', '0002_alter_pagament_datacad'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagament',
            name='actiu',
            field=models.BooleanField(default=False),
        ),
    ]