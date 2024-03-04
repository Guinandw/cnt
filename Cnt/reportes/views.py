import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .forms import ReportesForms
from cuentas.models import Usuarios, CNTs
from semana.models import Evento, Feriados
from semana.semana import Panel
# Create your views here.


@login_required
def reportesForm(request):
    reportesForm = ReportesForms(request.POST or None)
    contexto = { 'form':reportesForm}
    
    if request.method == 'GET':
        return render(request, template_name='reportes/reportes-form.html', context=contexto)
    else:
        if reportesForm.is_valid():
            inicio = reportesForm.cleaned_data['fechaInicio']
            fin = reportesForm.cleaned_data['fechaFin']
            print(inicio)
            print(fin)
            return redirect('reportes', fechaInicio=inicio, fechaFin=fin)
        else:
             messages.warning(request, reportesForm.errors)
             return render(request, template_name='reportes/reportes-form.html', context=contexto)

@login_required
def reportes(request, fechaInicio, fechaFin):
    
    usuarioAcceso, usuarioUrbano, usuarioInteru = [],[],[]
    
    eventos = None
    userAll = Usuarios.objects.all()
    
    usuarioAcceso = userAll.filter(equiposdetrabajos__cnt=CNTs.objects.get(id=1))
    usuarioUrbano = userAll.filter(equiposdetrabajos__cnt=CNTs.objects.get(id=2))
    usuarioInteru = userAll.filter(equiposdetrabajos__cnt=CNTs.objects.get(id=3))
    usuarioTellabs = userAll.filter(equiposdetrabajos__cnt=CNTs.objects.get(id=4))
    usuarioRadio = userAll.filter(equiposdetrabajos__cnt=CNTs.objects.get(id=7))
    usuarioSincro = userAll.filter(equiposdetrabajos__cnt=CNTs.objects.get(id=5))
    
    eventos = Evento.objects.filter(diaInicio__range=(fechaInicio, fechaFin))
        
        
    eventosAcceso =  eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=1))
    eventosUrbano =  eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=2))
    eventosInteru =  eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=3))
    eventosTellabs =  eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=4))
    eventosRadio =  eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=7))
    eventoSincro = eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=5))
    
    eventosGN = eventos.filter(tipoEvento='GUARDIA NOCHE')
    disponibilidades = eventos.filter(tipoEvento='DISPONIBILIDAD', profesional__is_supervisor=True)
    gn = []
    disp = []
    
    for e in eventos:
        print(e.profesional.first_name)
        print(e.tipoEvento)
        print(e.diaInicio)
        print(e.diaFin)
        print(e.inicioRealdeEvento())
        print(e.finRealdeEvento())
    
            
    
    for e in eventos:
        if e.evento_hoy():
            """ print(e.profesional.first_name)
            print(e.tipoEvento)
            print(e.diaInicio)
            print(e.inicioRealdeEvento())
            print(e.finRealdeEvento()) """
           
            gn.append(e)
        
    for e in disponibilidades:
        if e.evento_hoy():
            disp.append(e)
    
            
    feriados = Feriados.objects.all()

    panelAcceso = Panel(eventosAcceso, usuarioAcceso,feriados)
    panelUrbano = Panel(eventosUrbano, usuarioUrbano, feriados)
    panelInteru = Panel(eventosInteru, usuarioInteru, feriados)
    panelTellabs = Panel(eventosTellabs, usuarioTellabs, feriados)
    panelRadio = Panel(eventosRadio, usuarioRadio, feriados)
    panelSincro = Panel(eventoSincro, usuarioSincro, feriados)
    
   
    return redirect('inicio')