from django.urls import path
from Inicio.views import inicio, subir_recomendacion, buscar_recomendacion, acerca_mi

# app_name = "Inicio"

urlpatterns = [
    path('', inicio, name="inicio"),
    path("subir-recomendacion/", subir_recomendacion, name="subir_recomendacion"),
    path("buscar-recomendacion/", buscar_recomendacion, name="buscar_recomendacion"),
    path("acerca_mi/", acerca_mi, name="acerca_mi"),
]