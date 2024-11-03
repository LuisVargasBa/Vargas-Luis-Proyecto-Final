# Generated by Django 5.1.2 on 2024-11-01 16:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='anio',
            new_name='puntuacion',
        ),
        migrations.AddField(
            model_name='anime',
            name='fecha_de_emision',
            field=models.DateField(default=datetime.datetime(2024, 11, 1, 16, 8, 16, 80633, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]