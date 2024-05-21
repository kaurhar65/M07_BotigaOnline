# Generated by Django 5.0.6 on 2024-05-16 16:58

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('quantitat', models.IntegerField()),
                ('preu', models.DecimalField(decimal_places=2, max_digits=10, max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('descripcio', models.TextField()),
                ('dataCad', models.DateField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('actiu', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Cataleg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actiu', models.BooleanField(default=False)),
                ('preuTotal', models.DecimalField(decimal_places=2, max_digits=10, max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('producte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cataleg.producte')),
            ],
        ),
    ]