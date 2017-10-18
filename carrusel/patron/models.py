from django.db import models

class Contenido(models.Model):
    imagen = models.URLField()
    descripcion = models.CharField(max_length=200)
    url = models.URLField()
    titulo = models.CharField(max_length=25)

class Carrusel(models.Model):
    cantidad_elementos = models.IntegerField(default=2)
    pos_actual = models.IntegerField(default=0)
    tiempo_transicion = models.IntegerField(default=5)
    es_automatico = models.BooleanField()
    es_circular = models.BooleanField()
    elementos = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
