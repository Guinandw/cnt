from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login as cnt_login

from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages



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

def registro(request):
    return render(request, 'cuentas/register.html')