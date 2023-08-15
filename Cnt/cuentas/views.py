from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login as cnt_login
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

from django.views.generic import CreateView, UpdateView, ListView

from .form import CrearUsuarioForm
from .models import Usuarios




# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, template_name='cuentas/login.html')
    else:
        
        usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print(request.POST['username'])
        print(request.POST['password'])
        print(usuario)
        if usuario is None:
            messages.warning(request, 'Usuario o password Incorrecto')
            return render(request, 'cuentas/login.html')
        
        else:
            cnt_login(request, usuario)
            return render(request, 'publica/inicio.html')
            
@login_required
def salir(request): 
    logout(request)
    return render(request, 'publica/inicio.html')

def crearCuentas(request):
    if request.method == 'GET':
        return render(request, 'cuentas/register.html',)

class CrearCuentas(CreateView):
    model = Usuarios
    form_classs = UserCreationForm
    template_name = 'cuentas/register.html'
    success_url = reverse_lazy('inicio')
    


def perfil(request):
    return render(request, 'cuentas/profile.html')