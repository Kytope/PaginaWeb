# Generated by Django 4.1.6 on 2023-10-10 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiProyecto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='fecha_reserva',
            field=models.DateField(default='2023-01-01'),
        ),
    ]
