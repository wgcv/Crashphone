from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from cliente.models import *

class Registrar(UserCreationForm):
	#password = forms.CharField(widget=forms.PasswordInput())
	username = forms.CharField(
        max_length=150,
        label = 'Usuario'
    )
	first_name = forms.CharField(
		max_length=150,
		label = 'Nombre'
    )
	last_name = forms.CharField(
		max_length=150,
		label = 'Apellido'
    )
	email = forms.CharField(
		max_length=150,
		label = 'Correo'
    )
   
	class Meta:
			model = User
			fields = ('username','first_name','last_name','email')

class UserProfileForm(forms.ModelForm):
	foto = forms.FileField()
	class Meta:
		model = Cliente
		fields = ('celular','foto')