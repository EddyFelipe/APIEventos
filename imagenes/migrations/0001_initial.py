# Generated by Django 2.2.5 on 2019-10-07 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='')),
                ('eliminado', models.BooleanField(default=False)),
                ('codigoEvento', models.CharField(max_length=50)),
            ],
        ),
    ]
