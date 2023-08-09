from .models import Profesionales, Supervisores
from django import forms
from django.forms import ValidationError
import re


class CrearUsuarioForm(forms.ModelForm):
    
    
    class Meta:
        model = Profesionales
        fields = all


