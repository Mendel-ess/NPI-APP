# Generated by Django 4.2.5 on 2023-10-09 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=1000)),
                ('imagen', models.ImageField(upload_to='movies')),
                ('categorias', models.CharField(choices=[('C', 'COMEDIA'), ('D', 'DRAMA'), ('R', 'ROMANTICA'), ('A', 'ACCION')], max_length=1)),
                ('idioma', models.CharField(choices=[('ES', 'ESPAÑOL'), ('EN', 'INGLES')], max_length=2)),
                ('estado', models.CharField(choices=[('MC', 'MEJOR CALIFICADA'), ('MV', 'MAS VISTA'), ('AR', 'AÑADIDA RECIENTEMENTE')], max_length=2)),
                ('año_salida', models.DateField()),
                ('vistas', models.IntegerField(default=0)),
            ],
        ),
    ]
