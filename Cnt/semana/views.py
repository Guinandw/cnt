from django.shortcuts import render,redirect
from django.contrib import messages
from .semana import Semanas
import datetime
from .forms import DateForm
from .models import Semana



# Create your views here.

def cargarSemana(request):
    
    if request.method == 'GET':
        return render(request, template_name='semana/cargar-semana.html')
    else:
        form = DateForm(request.POST)
        if form.is_valid():
            print('cargar semana is valid')
            sem = Semana()
            sem.primer = form.cleaned_data['inicio']
            sem.ultimo = form.cleaned_data['fin']
            sem.detalles = sem.add_detalles()
            print(sem.primer)
            print(sem.detalles)
            sem.save()
            return render(request, template_name='semana/cargar-semana.html')
        else:
            messages.warning(request,form.errors)
            return render(request, template_name='semana/cargar-semana.html')
    
def cargarFeriado(request, semId:int):
    semF = Semana.objects.get(pk=semId)
    print(semF.detalles)
    if request.method == 'POST':
        if request.POST['feriado']:
            feriado = request.POST['feriado']
            if feriado >= semF.primer and feriado <= semF.ultimo:
                semF.agregar_feriado(feriado)
                messages.info(request, 'Para terminar click en Guardar')
                return render(request, template_name='semana/cargar-feriado.html', context={'sem':semF})
            else:
                messages.warning(request, 'Feriado no esta dentro de la semana que se esta cargando')
        else:
            messages.warning(request, 'Completar Datos o Guardar')
    
    return render(request, template_name='semana/cargar-feriado.html', context={'sem':semF})


def guardarSemana():
     
    return redirect('inicio')
    