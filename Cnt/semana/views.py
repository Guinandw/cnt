from django.shortcuts import render,redirect, resolve_url
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from .forms import EventoForm, FeriadosForm
from cuentas.models import Usuarios, equiposDeTrabajos
from .models import Evento, Feriados

from django.core.exceptions import EmptyResultSet



# Create your views here.
@login_required
def evento(request):
    #VISTA NO SE ESTA USANDO
    
    print(request.user.id)
    usuario = Usuarios.objects.get(pk=request.user.id)
    eventos = Evento.objects.filter(profesional__pk = request.user.id)
    form = EventoForm(request.POST or None)
    if request.method == 'GET':
        contexto= {'titulo':'Cargar Evento', 'form':form, 'usuario': usuario, 'eventos':eventos}
        return render(request, template_name='semana/cargar-evento.html', context=contexto)
    else:
        if form.is_valid():
            
            usuario = Usuarios.objects.get(pk=request.user.id)
            e = Evento()
            e.profesional = usuario
            e.tipoEvento = form.cleaned_data['tipoEvento']
            e.diaInicio = form.cleaned_data['diaInicio']
            e.diaFin = form.cleaned_data['diaFin']
            e.horaInicio = form.cleaned_data['horaInicio']
            e.duracion = form.cleaned_data['duracion']
            e.save()
            messages.info(request, 'Evento creado satisfactoriamente')
            
            
        else:
             messages.warning(request, form.errors)
             
        return render(request, template_name='semana/cargar-evento.html')
    
@login_required
def eventoId(request, userId):
    #VISTA PARA CREACION DE EVENTOS
    
    
    try:
        usuario = Usuarios.objects.get(pk=userId)
        eventos = Evento.objects.filter(profesional__pk = usuario.id)
    except:
        usuario = False
        eventos = False
    
    
       
    form = EventoForm(request.POST or None)
    contexto= {'titulo':'Cargar Evento', 'form':form, 'usuario': usuario, 'eventos':eventos}
    if request.method == 'GET':
        
        return render(request, template_name='semana/cargar-evento.html', context=contexto)
    else:
        if form.is_valid():
            
            
            e = Evento()
            e.profesional = usuario
            e.tipoEvento = form.cleaned_data['tipoEvento']
            e.diaInicio = form.cleaned_data['diaInicio']
            e.diaFin = form.cleaned_data['diaFin']
            e.horaInicio = form.cleaned_data['horaInicio']
            e.duracion = form.cleaned_data['duracion']
            e.save()
            messages.info(request, 'Evento creado satisfactoriamente')
            
            return redirect('lista-evento', userId=e.profesional.id)
            
        else:
             messages.warning(request, form.errors)
             return render(request, template_name='semana/cargar-evento.html', context=contexto)
        


#SE NECESITA QUE SOLO LOS SUPERVISORES PUEDAN ACCEDER A ESTA PAGINA    
@login_required
def listaCargarEvento(request):
    equipos = equiposDeTrabajos.objects.all()
    acceso = equipos.filter(cnt__nombre=1)
    urbano = equipos.filter(cnt__nombre=2)
    interurbano = equipos.filter(cnt__nombre=3)
    tellabs = equipos.filter(cnt__nombre=4)
    radio = equipos.filter(cnt__nombre=5)
    sincro = equipos.filter(cnt__nombre=6)
    
    
    contexto= {'acceso':acceso,'urbano':urbano, 'interu': interurbano, 'tellabs':tellabs, 'radio':radio, 'sincro':sincro}
    
    return render(request, 'semana/listaCargarEvento.html', context=contexto)

def listaEvento(request, userId):
    
    try:
        usuario = Usuarios.objects.get(pk=userId)
        eventos = Evento.objects.filter(profesional__pk = usuario.id).order_by('-diaInicio').values()
    except:
        usuario = False
        eventos = False
    contexto= {'titulo':'Lista de Evento', 'eventos':eventos, 'usuario':usuario}
    return render(request, 'semana/listarEventos.html', context=contexto)


def eliminarEvento(request, id):
    evento = Evento.objects.get(pk=id)
    userid = evento.profesional.id
    #print(f'se borro evento: {evento.id}' )
    evento.delete()
    return redirect('lista-evento', userId=userid)

@login_required
def listarFeriados(request):
    #FALTA ORDENAR LOS FERIADOS DESCENDIENTES
    feriados = Feriados.objects.all().order_by('-fecha').values()
    context = {'titulo':'Lista de Feriados', 'feriados':feriados}
    return render(request, template_name='semana/listarFeriados.html', context=context)

@login_required
def cargarFeriados(request):
    feriadosForm = FeriadosForm(request.POST or None)
    contexto = {'titulo':'Cargar Feriados', 'form':feriadosForm}
    
    if request.method == 'GET':
        return render(request, template_name='semana/cargar-feriado.html', context=contexto)
    else:
        if feriadosForm.is_valid():
            feriadosForm.save()
            return redirect('listar-feriados')
        #return render(request, 'semana/cargar-feriado.html', context=contexto)

@login_required
def eliminarFeriados(request, feriadoId):
    feriado = Feriados.objects.get(pk=feriadoId)
    feriado.delete()
    return redirect('listar-feriados')