from django import forms
from Mensajes.models import Mensaje

class Mensajeria(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['usuario_recibe', 'contenido_mensaje']
