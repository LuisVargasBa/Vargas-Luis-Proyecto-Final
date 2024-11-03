from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from Usuarios.forms import FormCreacionUsuario, FormEditarPerfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from Usuarios.models import AvatarPerfil, FavoritoPerfil

def Login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            
            django_login(request, usuario)
            
            AvatarPerfil.objects.get_or_create(user=usuario)
            FavoritoPerfil.objects.get_or_create(user=usuario)
                                 
            return redirect('Inicio:inicio')
    
    return render(request, 'Usuarios/login.html', {'form': formulario})

def registro(request):
    
    formulario = FormCreacionUsuario()
    
    if request.method == 'POST':
        formulario = FormCreacionUsuario(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect ("Usuarios:login")
    
    return render (request, "Usuarios/registro.html", {"form": formulario })

@login_required
def ver_perfil(request):
    usuario = request.user
    avatar_perfil = AvatarPerfil.objects.filter(user=usuario).first()  
    favorito_perfil = FavoritoPerfil.objects.filter(user=usuario).first() 

    contexto = {
            'usuario': usuario,
            'avatar': avatar_perfil.avatar if avatar_perfil else None,
            'favorito': favorito_perfil.favorito if favorito_perfil else None,
        }

    return render(request, 'Usuarios/ver_perfil.html', contexto)

@login_required
def editar_perfil(request):
    avatar_perfil, created = AvatarPerfil.objects.get_or_create(user=request.user)
    
    favorito_perfil, created = FavoritoPerfil.objects.get_or_create(user=request.user)
    
    formulario = FormEditarPerfil(instance=request.user, initial={"avatar": avatar_perfil.avatar, "favorito": favorito_perfil.favorito})
    
    if request.method == "POST":
        formulario = FormEditarPerfil(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            
            avatar_nuevo = formulario.cleaned_data.get("avatar")
            if avatar_nuevo:
                avatar_perfil.avatar = avatar_nuevo
            avatar_perfil.save()
            
            favorito_nuevo = formulario.cleaned_data.get("favorito")
            if favorito_nuevo:
                favorito_perfil.favorito = favorito_nuevo
            favorito_perfil.save()
            
            formulario.save()
            
            return redirect('Inicio:inicio')
    
    return render (request, "Usuarios/editar_perfil.html", {"form": formulario})


class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'Usuarios/cambiar_password.html'
    success_url = reverse_lazy('Usuarios:editar_perfil')