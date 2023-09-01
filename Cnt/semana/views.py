from django.shortcuts import render,redirect
from django.contrib import messages
from .semana import Semanas
import datetime
from .forms import DateForm
from . import models



# Create your views here.

def cargarSemana(request):
    
    if request.method == 'GET':
        return render(request, template_name='semana/cargar-semana.html')
    else:
        form = DateForm(request.POST)
        if form.is_valid():
            inicio = form.cleaned_data['inicio']
            fin = form.cleaned_data['fin']
            sem = Semanas(inicio, fin)
            models.Semana()
            return render(request, template_name='semana/cargar-feriado.html', context={'sem':sem})
        return render(request, template_name='semana/cargar-semana.html')
    
def cargarFeriado(request, sem:Semanas):
    print(sem.dias)
    if request.method == 'POST':
        if request.POST['feriado']:
            feriado = request.POST['feriado']
            if feriado >= sem.inicio and feriado <= sem.fin:
                sem.agregar_feriado(feriado)
                messages.info(request, 'Para terminar click en Guardar')
                return render(request, template_name='semana/cargar-feriado.html', context={'sem':sem})
            else:
                messages.warning(request, 'Feriado no esta dentro de la semana que se esta cargando')
        else:
            messages.warning(request, 'Completar Datos o Guardar')
    
    return render(request, template_name='semana/cargar-feriado.html', context={'sem':sem})


def guardarSemana(sem:Semanas):
    semana = models.Semana()
    semana.primer = sem.inicio
    semana.ultimo = sem.fin
    semana.detalles = sem.dias
    semana.save()
    print(sem.dias)
    return redirect('inicio')
    