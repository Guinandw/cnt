from django.shortcuts import render
from django.http import request
from cuentas.models import Usuarios, equiposDeTrabajos, CNTs
from semana.models import Evento, Feriados
from semana.semana import Panel, hoy, ahora
from django.db.models import Q
import datetime


# Create your views here.
def inicio(request):
    userAll = Usuarios.objects.all()
    
    usuarioAcceso = userAll.filter(equiposdetrabajos__cnt=CNTs.objects.get(id=1))
    usuarioUrbano = userAll.filter(equiposdetrabajos__cnt=CNTs.objects.get(id=2))
    usuarioInteru = userAll.filter(equiposdetrabajos__cnt=CNTs.objects.get(id=3))
    
    eventos = Evento.objects.filter(diaInicio__gt=datetime.datetime.now().date()-datetime.timedelta(days=8))
    """ for e in eventosAcceso:
        print(e.profesional.first_name)
        print(e.diaInicio)
        print(e.horaInicio)
        print(type(e.horaInicio))  """
        
    eventosAcceso =  eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=1))
    eventosUrbano =  Evento.objects.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=2))
    eventosInteru =  Evento.objects.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=3))

    feriados = Feriados.objects.all()

    panelAcceso = Panel(eventosAcceso, usuarioAcceso,feriados)
    panelUrbano = Panel(eventosUrbano, usuarioUrbano, feriados)
    panelInteru = Panel(eventosInteru, usuarioInteru, feriados)
    
    
    
    
    onlineAcceso = panelAcceso.online()
    onlineUrbano = panelUrbano.online()
    onlineInteru = panelInteru.online()
    """ for e in onlineAcceso:
        print(e.profesional.first_name)
        print(e.tipoEvento)
        print(e.diaInicio)
        print(e.inicioRealdeEvento())
        print(e.finRealdeEvento())
        print(e.inicioDeEventoHoy())
        print(e.finDeEventoHoy())
        if e.inicioDeEventoHoy() <= ahora and ahora <= e.finDeEventoHoy():
            print('ONLINE')
        else:
            print('OFFLINE')
        print('\n') """
    contexto= {'acceso':onlineAcceso,'urbano':onlineUrbano, 'interu': onlineInteru}
    #pequeño script para corregir horarios de salida
    """ for a in acceso:
        a.miembro.save_horaSalida()
        print(a.miembro.first_name)
        print(a.miembro.preferenciaHorario)
        print(a.miembro.horaSalida())
    for u in urbano:
        u.miembro.save_horaSalida()
    for i in interurbano:
        i.miembro.save_horaSalida() """
    return render(request, 'publica/inicio-copy.html', context=contexto)