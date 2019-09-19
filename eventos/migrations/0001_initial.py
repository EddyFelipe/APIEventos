# Generated by Django 2.2.4 on 2019-09-19 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=40)),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('direccion', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField()),
                ('disponible', models.BooleanField(default=False)),
                ('rutaLugar', models.CharField(max_length=150)),
                ('calificacionP', models.IntegerField(default=0)),
                ('eliminado', models.BooleanField(default=False)),
                ('id_departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.Departamento')),
            ],
            options={
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='')),
                ('id_evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='eventos.Evento')),
            ],
        ),
    ]
