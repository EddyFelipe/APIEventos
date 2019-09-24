# Generated by Django 2.2.5 on 2019-09-24 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localidades', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='localidad',
            old_name='canitidadAsientosDisponible',
            new_name='cantidadAsientosDisponible',
        ),
        migrations.RemoveField(
            model_name='localidad',
            name='idEventos',
        ),
        migrations.AddField(
            model_name='localidad',
            name='codigoEventos',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
