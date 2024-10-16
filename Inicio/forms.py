from django import forms

class IngresarAnime(forms.Form):
    nombre = forms.CharField(max_length=60)
    genero = forms.CharField(max_length=60)
    personaje = forms.CharField(max_length=60)
    anio = forms.IntegerField()
    
class BuscarAnime(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    genero = forms.CharField(max_length=20, required=False)