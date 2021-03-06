# Generated by Django 2.2.5 on 2019-11-14 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0001_initial'),
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
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('disponible', models.BooleanField(default=False)),
                ('rutaLugar', models.CharField(max_length=150)),
                ('calificacionP', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
                ('contcomment', models.IntegerField(default=0)),
                ('sumcalificacion', models.IntegerField(default=0)),
                ('eliminado', models.BooleanField(default=False)),
                ('idDepartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.Departamento')),
            ],
            options={
                'ordering': ['fecha'],
            },
        ),
    ]
