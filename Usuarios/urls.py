from django.urls import path
from Usuarios import views
from django.contrib.auth.views import LogoutView


app_name = "Usuarios"

urlpatterns = [
    path("login/", views.Login, name="login"),
    path("registro/", views.registro, name="registro"),
    path("logout/", LogoutView.as_view(template_name = "Usuarios/logout.html"), name="logout"),
    path("perfil/ver", views.ver_perfil, name="ver_perfil"),
    path("perfil/editar", views.editar_perfil, name="editar_perfil"),
    path("perfil/editar/contraseña", views.CambiarPassword.as_view(), name="cambiar_password"),
]