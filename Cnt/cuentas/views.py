from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login as cnt_login
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages

from django.views.generic import CreateView, UpdateView, ListView

from .form import CrearUsuarioForm, CambiarPasswordForm, EditarUsuarioForm
from .models import Usuarios, equiposDeTrabajos, NOMBRES




# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, template_name='cuentas/login.html')
    else:
        #vease que el username se pasa a minusculas
        usuario = authenticate(request, username=str(request.POST['username']).lower(), password=request.POST['password'])
        
        if usuario is None:
            messages.warning(request, 'Usuario o password Incorrecto')
            return render(request, 'cuentas/login.html')
        
        else:
            if usuario.is_active:
                cnt_login(request, usuario)
                return redirect('inicio')
            else:
                messages.warning(request, 'Cuenta Desactivada')
            return redirect('login')
        
@login_required
def salir(request): 
    logout(request)
    return redirect('inicio')


def crearCuentas(request):
    if request.method == 'GET':
        return render(request, 'cuentas/register.html')
    else:
        
        userForm = CrearUsuarioForm(request.POST)
        
        userForm.username = str(request.POST['username']).lower()
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
                usuario.save_horaSalida()
                
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
    try:
        cnt = equiposDeTrabajos.objects.filter(usuarios = usuario)
    except:
        cnt = False
    return render(request, 'cuentas/profile.html', context={'usuario': usuario, 'cnts':cnt})

@login_required
def cambiar_password(request):
    if request.method == 'POST':
        form = CambiarPasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            
            update_session_auth_hash(request, user)
            messages.success(request, ('La contraseña ha sido actualizada'))
            logout(request)
            return redirect('login')
        else:
            messages.error(request, ('Favor verificar:'))
    else:
        form = CambiarPasswordForm(request.user)
    return render(request, 'cuentas/cambiar_password.html', {
        'form': form})
    

@login_required
def editar_perfil(request):
    usuario = Usuarios.objects.get(pk=request.user.id)
    
    if request.method == 'GET':
        form = EditarUsuarioForm(instance=usuario)
        return render(request, 'cuentas/editar_perfil.html', {'form':form})
    else:
        userForm = EditarUsuarioForm(request.POST, instance=usuario)
        
        userForm.email = request.POST['email']
        userForm.first_name = request.POST['first_name']
        userForm.last_name = request.POST['last_name']
        userForm.telefono = request.POST['telefono']
        userForm.movil = request.POST['movil']
        userForm.preferenciaHorario = request.POST['preferenciaHorario']
        userForm.horasXdia = request.POST['horasXdia']
        #userForm.legajo = request.POST['legajo']
      
        if userForm.is_valid():
                
                usuario = userForm.save(commit=False)
                usuario.save_horaSalida()
                #usuario.save()
                messages.success(request, f'Cambios Guardados')
            
        else:
            messages.warning(request, userForm.errors)
            form = EditarUsuarioForm(instance=usuario)
            return render(request, 'cuentas/editar_perfil.html', {'form':form})
        return redirect('perfil')