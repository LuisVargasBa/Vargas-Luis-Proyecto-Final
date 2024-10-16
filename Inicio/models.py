from django.db import models


class Anime(models.Model):
    nombre = models.CharField(max_length=60)
    genero = models.CharField(max_length=25)
    personaje = models.CharField(max_length=40)
    anio = models.IntegerField()
        
    def __str__(self):
        return f'{self.nombre} {self.genero}'