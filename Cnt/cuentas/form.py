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
            print('error nombre')
            raise ValidationError(f'{value} no es un nombre valido', code='Invalid', params={'valor':value})
    
        
def validador_numeros(value):
    print('VALIDADOR NUMERO')
    for i in value:
        if (i.isdigit()):
            pass
        else: 
            print('error numero')
            raise ValidationError(f'No ingrese ni letras ni signos.', code='Invalid', params={'valor':value})
        
def validador_email(value):
    print('VALIDADOR EMAIL')
    email_regex = r'^[a-zA-Z0-9._%+-]+@telefonica.com'
    if not re.match(email_regex, value):
        print('error correo')
        raise ValidationError('Correo electrónico inválido')
    return value


PREFERENCIAS = [
        (1, '7'),
        (2, '8'),
        (3, '9'),
        (4,'10'),
        (5,'11'),
        (6,'12'),
        (7,'13'),
        (8, '14'),
        
    ]
    
NOMBRES = [
        (1, 'Acceso'),
        (2, 'Urbano'),
        (3,'Interurbano'),
        (4,'Tellabs'),
        (5, 'Radio'),
        (6,'Sincronismo'),
        (7,'Soporte')
    ]
    
HORASXDIA = [
        (1,'7'),
        (2,'8'),
        (3,'9'),
    ]
    

class CrearUsuarioForm(forms.ModelForm):
    
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
    
    legajo = forms.CharField(
        label='Legajo',
        max_length=6,
        validators=(validador_numeros,),
        required=False,
    )
    
    telefono = forms.CharField(
        label='Telefono',
        max_length=11,
        validators=(validador_numeros,),
        
    )
    
    movil = forms.CharField(
        label='Movil',
        max_length=11,
        validators=(validador_numeros,),
    )
    
    preferenciaHorario = forms.ChoiceField(
        label='Preferencia Inicio Jornada',
        choices=PREFERENCIAS,
    )

    horasXdia = forms.ChoiceField(
        label='Horas por Jornada',
        choices=HORASXDIA,
    )
    
    """ def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user """
    
    class Meta:
        model = Usuarios
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'telefono', 'movil', 'preferenciaHorario', 'horasXdia']    
        

