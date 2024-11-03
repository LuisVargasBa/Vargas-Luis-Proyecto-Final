from django import forms
from .models import Anime

class BaseFormAnime(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ["nombre", "genero", "personaje", "puntuacion", "fecha_de_emision", "imagen"]

class IngresarAnime(BaseFormAnime):
    ...
       
class EditarAnime(BaseFormAnime):
    ...


class BuscarAnime(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    genero = forms.CharField(max_length=20, required=False)