# Generated by Django 5.0.6 on 2024-05-23 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagament', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagament',
            name='dataCad',
            field=models.CharField(max_length=5),
        ),
    ]