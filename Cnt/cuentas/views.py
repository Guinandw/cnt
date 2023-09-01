from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login as cnt_login
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages

from django.views.generic import CreateView, UpdateView, ListView

from .form import CrearUsuarioForm
from .models import Usuarios, equiposDeTrabajos, NOMBRES




# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, template_name='cuentas/login.html')
    else:
        print(str(request.POST['username']).lower())
        usuario = authenticate(request, username=str(request.POST['username']).lower(), password=request.POST['password'])
        print(request.POST['username'])
        print(request.POST['password'])
        print(usuario)
        if usuario is None:
            messages.warning(request, 'Usuario o password Incorrecto')
            return render(request, 'cuentas/login.html')
        
        else:
            if usuario.is_active:
                cnt_login(request, usuario)
                return render(request, 'publica/inicio.html')
            else:
                messages.warning(request, 'Cuenta Desactivada')
            return render(request, 'cuentas/login.html')
@login_required
def salir(request): 
    logout(request)
    return render(request, 'publica/inicio.html')

def crearCuentas(request):
    if request.method == 'GET':
        return render(request, 'cuentas/register.html')
    else:
        
        userForm = CrearUsuarioForm(request.POST)
        
        userForm.username = str(request.POST['username']).lower
        userForm.email = request.POST['email']
        userForm.password1 = request.POST['password1']
        userForm.password2 = request.POST['password2']
        userForm.first_name = request.POST['first_name']
        userForm.last_name = request.POST['last_name']
        userForm.telefono = request.POST['telefono']
        userForm.movil = request.POST['movil']
        userForm.preferenciaHorario = request.POST['preferenciaHorario']
        userForm.horasXdia = request.POST['horasXdia']
        
      
        if userForm.is_valid():
            if userForm.password1 == userForm.password2:
                
                usuario = userForm.save(commit=False)
                usuario.set_password(userForm.password1)
                usuario.save()
                messages.success(request, f'Registrado Satisfactoriamente')
            else:
                messages.warning(request, 'Passwords incorrectos')
        else:
            messages.warning(request, userForm.errors)
            return render(request, 'cuentas/register.html')
        return render(request, template_name='cuentas/login.html')
        
 

@login_required
def perfil(request):
    usuario = Usuarios.objects.get(pk=request.user.id)
    cnt = equiposDeTrabajos.objects.filter(miembro = usuario)
    print(cnt)
    return render(request, 'cuentas/profile.html', context={'usuario': usuario, 'cnts':cnt})