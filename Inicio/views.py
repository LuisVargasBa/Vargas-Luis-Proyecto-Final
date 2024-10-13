from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render

def mi_vista(request):
    return HttpResponse('Hola soy la vista')

def inicio(request):
    return HttpResponse('<h1>Soy la pantalla de inicio </h1>')
    # return render(request, 'inicio/index.html')