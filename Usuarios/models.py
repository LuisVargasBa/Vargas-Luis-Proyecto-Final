from django.db import models
from django.contrib.auth.models import User

class AvatarPerfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="Avatares", blank= True, null= True)
    
class FavoritoPerfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorito = models.CharField(max_length=200)