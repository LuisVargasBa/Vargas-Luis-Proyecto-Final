from django.urls import path
from Inicio import views

app_name = "Inicio"

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path("Inicio/subir/", views.CrearRecomenda.as_view(), name="subir_recomendacion"),
    path("Inicio/buscar/", views.buscar_recomendacion, name="buscar_recomendacion"),
    path("Inicio/acerca-mi/", views.acerca_mi, name="acerca_mi"),
    path("Inicio/ingreso-correcto/", views.ingreso_correcto, name="ingreso_correcto"),
    path("Inicio/ver/<int:pk>", views.ListaRecomenda.as_view(), name="ver_recomendacion"),
    path("Inicio/eliminar/<int:pk>", views.EliminarRecomenda.as_view(), name="eliminar_recomendacion"),
    path("Inicio/editar/<int:id>", views.editar_recomenda, name="editar_recomendacion"),
]