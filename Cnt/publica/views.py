from django.shortcuts import render
from django.http import request
from cuentas.models import Usuarios, equiposDeTrabajos, CNTs
from semana.models import Evento, Feriados
from semana.semana import Panel
from django.db.models import Q
import datetime


# Create your views here.
def inicio(request):
    usuarioAcceso, usuarioUrbano, usuarioInteru = None,None,None
    
    eventos = None
    userAll = Usuarios.objects.all()
    
    usuarioAcceso = userAll.filter(equiposdetrabajos__cnt=CNTs.objects.get(id=1))
    usuarioUrbano = userAll.filter(equiposdetrabajos__cnt=CNTs.objects.get(id=2))
    usuarioInteru = userAll.filter(equiposdetrabajos__cnt=CNTs.objects.get(id=3))
    #supervisores = userAll.filter(is_supervisor=True)
    eventos = Evento.objects.filter(diaInicio__gt=datetime.datetime.now().date()-datetime.timedelta(days=8))
    
        
    eventosAcceso =  eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=1))
    eventosUrbano =  eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=2))
    eventosInteru =  eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=3))
    eventosGN = eventos.filter(tipoEvento='GUARDIA NOCHE')
    disponibilidades = eventos.filter(tipoEvento='DISPONIBILIDAD', profesional__is_supervisor=True)
    gn = []
    disp = []
    
    for e in eventosGN:
        if e.evento_hoy():
            print(e.profesional.first_name)
            print(e.tipoEvento)
            print(e.diaInicio)
            print(e.inicioRealdeEvento())
            print(e.finRealdeEvento())
           
            gn.append(e)
        
    for e in disponibilidades:
        if e.evento_hoy():
            disp.append(e)
    
            
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
        print('son las:'+ str(datetime.datetime.now()))
        if e.inicioDeEventoHoy() <= datetime.datetime.now() and datetime.datetime.now() <= e.finDeEventoHoy():
            print('ONLINE')
        else:
            print('OFFLINE')
        print('\n') """
    contexto= {'acceso':onlineAcceso,'urbano':onlineUrbano, 'interu': onlineInteru, 'noche': gn, 'disp':disp}
    #pequeño script para corregir horarios de salida
    """ for a in usuarioAcceso:
            a.save_horaSalida()
            
        for u in usuarioUrbano:
            u.save_horaSalida()
            
        for i in usuarioInteru:
            i.save_horaSalida()"""
    return render(request, 'publica/inicio-copy.html', context=contexto)