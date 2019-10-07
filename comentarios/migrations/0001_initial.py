# Generated by Django 2.2.5 on 2019-10-07 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('calificacion', models.IntegerField(default=0)),
                ('codigoEvento', models.CharField(max_length=50)),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to='usuarios.Usuario')),
            ],
        ),
    ]
