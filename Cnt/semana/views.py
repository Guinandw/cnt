from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from .forms import EventoForm
from cuentas.models import Usuarios
from .models import Evento



# Create your views here.
@login_required
def evento(request):
    form = EventoForm(request.POST or None)
    if request.method == 'GET':
        contexto= {'titulo':'Cargar Evento', 'form':form}
        return render(request, template_name='semana/cargar-evento.html', context=contexto)
    else:
        if form.is_valid():
            
            usuario = Usuarios.objects.get(pk=form.cleaned_data['profesional'])
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