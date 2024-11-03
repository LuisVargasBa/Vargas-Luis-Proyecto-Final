from django.template import Template, Context, loader
from django.shortcuts import render, redirect
from Inicio.models import Anime
from Inicio.forms import BaseFormAnime, BuscarAnime, EditarAnime, IngresarAnime
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


def inicio(request):
    return render(request, 'Inicio/index.html')
    

class CrearRecomenda(LoginRequiredMixin, CreateView):
    model = Anime
    template_name = "Inicio/subir_recomenda.html"
    success_url = reverse_lazy("Inicio:ingreso_correcto")
    form_class = BaseFormAnime
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
def buscar_recomendacion(request):
    
    formulario = BuscarAnime(request.GET)
    if formulario.is_valid():
            nombre = formulario.cleaned_data.get('nombre')
            genero = formulario.cleaned_data.get('genero')
            animes = Anime.objects.filter(nombre__icontains=nombre, genero__icontains=genero)
        
    return render(request, 'Inicio/buscar_recomenda.html', {'animes': animes, 'form': formulario})


def ingreso_correcto(request):
    return render(request, 'Inicio/ingreso_correcto.html')

class ListaRecomenda(DetailView):
    model = Anime
    template_name = "Inicio/ver_recomenda.html"

     
class EliminarRecomenda(LoginRequiredMixin, DeleteView):
    model = Anime
    template_name = "Inicio/eliminar_recomenda.html"
    success_url = reverse_lazy("Inicio:buscar_recomendacion")

@login_required
def editar_recomenda(request, id):
    anime = Anime.objects.get(id=id)
    
    formulario = EditarAnime(initial={
        "nombre": anime.nombre, 
        "genero": anime.genero,
        "personaje": anime.personaje,
        "puntuacion": anime.puntuacion,
        "fecha_de_emision": anime.fecha_de_emision,
        "imagen": anime.imagen,
    })
           
    if request.method == "POST":
        formulario = EditarAnime(request.POST, request.FILES, instance=anime)
        if formulario.is_valid():
            anime.nombre = formulario.cleaned_data.get("nombre")
            anime.genero = formulario.cleaned_data.get("genero")
            anime.personaje = formulario.cleaned_data.get("personaje")
            anime.puntuacion = formulario.cleaned_data.get("puntuacion")
            anime.fecha_de_emision = formulario.cleaned_data.get("fecha_de_emision")
            anime.imagen = formulario.cleaned_data.get("imagen")
            
            anime.save()

            return redirect('Inicio:buscar_recomendacion')
        
    return render(request, 'Inicio/editar_recomenda.html', {'anime': anime, 'form': formulario})
    

def acerca_mi(request):
    return render(request, 'Inicio/acerca_mi.html')

