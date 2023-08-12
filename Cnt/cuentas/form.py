from .models import Usuarios
from django import forms
from django.forms import ValidationError
import re


class CrearUsuarioForm(forms.ModelForm):
    
    
    class Meta:
        model = Usuarios
        exclude = ['is_supervisor']


