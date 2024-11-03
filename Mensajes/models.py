from django.contrib.auth.models import User
from django.db import models

class Mensaje(models.Model):
    usuario_envia = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    usuario_recibe = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    contenido_mensaje = models.TextField()
    hora_mensaje = models.DateTimeField(auto_now_add=True)
    visto = models.BooleanField(default=False)

    def __str__(self):
        return f"Mensaje del usuario {self.usuario_envia} para {self.usuario_recibe} a las {self.hora_mensaje}"

