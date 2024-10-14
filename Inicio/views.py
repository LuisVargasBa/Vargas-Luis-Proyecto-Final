from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render
from Inicio.models import Anime


# fecha_actual = datetime.now()
    # datos = {
    #     'fecha_actual': fecha_actual,          
    # }

def inicio(request):
    return render(request, 'index.html')
    
# def ingresar_anime(request, nombre, genero, personaje):
    
#     anime_ingresado = Anime(nombre=nombre, genero=genero, personaje=personaje)
#     anime_ingresado.save()
#     return render(request, 'Inicio/ingreso_correcto.html', {'anime': anime_ingresado})

def subir_recomendacion(request):
    
    # anime_ingresado = Anime(nombre=nombre, genero=genero, personaje=personaje)
    # anime_ingresado.save()
    print ("Request", request)
    
    return render(request, 'Inicio/subir_recomenda.html', {'anime': ""})
    
    
    
def buscar_recomendacion(request, nombre, genero, personaje):
    anime_ingresado = Anime(nombre=nombre, genero=genero, personaje=personaje)
    anime_ingresado.save()
    return render(request, 'Inicio/buscar_recomenda.html', {'anime': anime_ingresado})



def acerca_mi(request):
    return render(request, 'acerca_mi.html')

