from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render, redirect
from Inicio.models import Anime
from Inicio.forms import IngresarAnime, BuscarAnime


def inicio(request):
    return render(request, 'Inicio/index.html')
    

def subir_recomendacion(request):
    
    formulario = IngresarAnime()
    
    if request.method == "POST":
        formulario = IngresarAnime(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            anime_ingresado = Anime(nombre= data.get("nombre"), genero=data.get("genero"), personaje=data.get("personaje"), anio=data.get("anio"))
            anime_ingresado.save()
            return redirect ("Inicio:ingreso_correcto")
        
    return render(request, 'Inicio/subir_recomenda.html', {'form': formulario})
       
    
def buscar_recomendacion(request):
    
    formulario = BuscarAnime(request.GET)
    if formulario.is_valid():
            nombre = formulario.cleaned_data.get('nombre')
            genero = formulario.cleaned_data.get('genero')
            animes = Anime.objects.filter(nombre__icontains=nombre, genero__icontains=genero)
        
    return render(request, 'Inicio/buscar_recomenda.html', {'animes': animes, 'form': formulario})


def ingreso_correcto(request):
    return render(request, 'Inicio/ingreso_correcto.html')


def acerca_mi(request):
    return render(request, 'Inicio/acerca_mi.html')

