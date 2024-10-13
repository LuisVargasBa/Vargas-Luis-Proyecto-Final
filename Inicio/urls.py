from django.urls import path
from Inicio.views import mi_vista, inicio

app_name = 'inicio'

urlpatterns = [
    path('mi-vista/', mi_vista, name='mi_vista'),
    path('', inicio, name='inicio'),
]