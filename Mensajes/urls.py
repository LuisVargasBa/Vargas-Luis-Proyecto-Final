from django.urls import path
from Mensajes import views

app_name = "Mensajes"

urlpatterns = [
    path('inbox/', views.bandeja_mensaje, name='bandeja_mensajes'),
    path('send/', views.enviar_mensaje, name='enviar_mensajes'),
]
