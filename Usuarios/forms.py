from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class FormCreacionUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Cree una Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita su Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}

class FormEditarPerfil(UserChangeForm):
    email = forms.EmailField(label= "Correo electronico")
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    password = None
    avatar = forms.ImageField(label= "Sube un avatar para tu usuario", required=False)
    favorito = forms.CharField(label="Comparte tus generos de anime favoritos", required=False)
    
    class Meta():
        model = User
        fields = ['email', 'first_name', 'last_name', "favorito", "avatar"]
        

