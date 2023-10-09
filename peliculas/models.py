from django.db import models

# Create your models here.
IDIOMAS = {
        ('ES','ESPAÑOL'),
        ('EN', 'INGLES'),
    } 
ESTADO = {
        ('AR','AÑADIDA RECIENTEMENTE'),
        ('MV','MAS VISTA'),
        ('MC','MEJOR CALIFICADA')
    }
CATEGORIAS = {
        ('A','ACCION'),
        ('D', 'DRAMA'),
        ('C', 'COMEDIA'),
        ('R', 'ROMANTICA'),
        }
class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000)
    imagen = models.ImageField(upload_to='movies')
    categorias = models.CharField(choices=CATEGORIAS, max_length=1)
    idioma = models.CharField(choices=IDIOMAS, max_length=2)
    estado = models.CharField(choices=ESTADO, max_length=2)
    año_salida = models.DateField()
    vistas = models.IntegerField(default=0)
