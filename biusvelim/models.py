from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.
LIMITE = {
    ('Todos','Todos'),
    ('Niños','Niños')
}

CATEGORIAS = {
        ('A','ACCION'),
        ('D', 'DRAMA'),
        ('C', 'COMEDIA'),
        ('R', 'ROMANTICA'),
        }
IDIOMAS = {
        ('ES','ESPAÑOL'),
        ('EN', 'INGLES'),
    } 
class CustomUser(AbstractUser):
    perfiles = models.ManyToManyField('Perfil', blank=True)


class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    edad_limite = models.CharField(choices=LIMITE, max_length=10)
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    categorias = models.CharField(choices=CATEGORIAS, max_length=1)
    idioma = models.CharField(choices=IDIOMAS, max_length=2)
    video = models.ManyToManyField('Video')
    imagen = models. ImageField(upload_to='cover')
    edad_limite = models.CharField(choices=LIMITE, max_length=10)

    def __str__(self):
        return self.titulo
    
class Video(models.Model):
        titulo = models.CharField(max_length=1000)
        archivo = models.FileField(upload_to='movies')

        def __str__(self):
            return self.titulo   





