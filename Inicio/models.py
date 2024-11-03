from django.db import models
from django.contrib.auth.models import User

class Anime(models.Model):
    nombre = models.CharField(max_length=60)
    genero = models.CharField(max_length=25)
    personaje = models.CharField(max_length=30)
    puntuacion = models.IntegerField()
    fecha_de_emision = models.DateField()
    imagen = models.ImageField(upload_to="Imagenes", blank= True, null= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
            
    def __str__(self):
        return f"Anime : {self.nombre} Genero: {self.genero}"
    
