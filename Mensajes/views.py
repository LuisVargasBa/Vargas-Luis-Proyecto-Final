from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Mensajes.models import Mensaje
from Mensajes.forms import Mensajeria
from django.contrib.auth.models import User

@login_required
def bandeja_mensaje(request):
    mensajes = Mensaje.objects.filter(usuario_recibe=request.user)
    return render(request, 'Mensajes/bandeja_mensajes.html', {'mensajes': mensajes})

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        formulario = Mensajeria(request.POST)
        if formulario.is_valid():
            mensaje = formulario.save(commit=False)
            mensaje.usuario_envia = request.user
            mensaje.save()
            return redirect('Mensajes:bandeja_mensajes')
    else:
        formulario = Mensajeria()
    return render(request, 'Mensajes/enviar_mensajes.html', {'form': formulario})

