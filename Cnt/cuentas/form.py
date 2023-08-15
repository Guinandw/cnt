from typing import Any
from .models import Usuarios
from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
import re

def validador_nombres(value):
    print('VALIDADOR NOMBRE')
    for i in value:
        if (i.isdigit()):
            raise ValidationError(f'{value} no es un nombre valido', code='Invalid', params={'valor':value})
    
        
def validador_numeros(value):
    print('VALIDADOR NUMERO')
    for i in value:
        if (i.isdigit()):
            pass
        else: raise ValidationError(f'No ingrese ni letras ni signos.', code='Invalid', params={'valor':value})
        
def validador_email(value):
    print('VALIDADOR EMAIL')
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError('Correo electrónico inválido')
    return value


class CrearUsuarioForm(forms.ModelForm):
    
    
    NOMBRES = [
        (1, 'Acceso'),
        (2, 'Urbano'),
        (3,'Interurbano'),
        (4,'Tellabs'),
        (5, 'Radio'),
        (6,'Sincronismo'),
    ]
    
    
    username = forms.CharField(
        label='Nombre de Usuario',
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Alias...'})
    )
    
    password1 = forms.CharField(
        label='Password',
        required=True,
        max_length=100,
        min_length=8,
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
    
    password2 = forms.CharField(
        label='Confirmar Password',
        required=True,
        max_length=100,
        min_length=8,
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
    
    email = forms.EmailField(
        max_length=200, 
        label='Correo',
        validators=(validador_email,),
        error_messages={ 
                        "required":'Correo Invalido'},
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Correo', 'type':'email'})
        )
    
    first_name = forms.CharField(
        label='Nombre',
        required=True,
        max_length=100,
        validators=(validador_nombres,),
        error_messages={'required':'probando'},
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre...'})
    )
    
    last_name = forms.CharField(
        label='Apellido',
        max_length=100,
        validators=(validador_nombres,),
        error_messages={'required':'probando'},
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido...'})
    )
    
    legajo = forms.TextInput(
        label='Legajo',
        max_length=6,
        validators=(validador_numeros),
    )
    
    telefono = forms.TextInput(
        label='Telefono',
        max_length=10,
        validators=(validador_numeros),
        
        
    )
    
    telefono = forms.TextInput(
        label='Movil',
        max_length=10,
        validators=(validador_numeros),
        
        
    )
    
    preferenciaHorario= 
    
    
    
    
    class Meta:
        model = Usuarios
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
        


