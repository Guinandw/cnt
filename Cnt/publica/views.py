import datetime

from django.db.models import Q
from django.shortcuts import render
from django.http import request

from cuentas.models import Usuarios, CNTs
from semana.models import Evento, Feriados
from semana.semana import Panel
from reportes.reporte import Test

# Create your views here.
def inicio(request):
    #test = Test()
    #test.prueba()
    usuarioAcceso, usuarioUrbano, usuarioInteru = [],[],[]
    
    eventos = None
    userAll = Usuarios.objects.all()
    
    usuarioAcceso = userAll.filter(equiposdetrabajos__cnt=CNTs.objects.get(id=1))
    usuarioUrbano = userAll.filter(equiposdetrabajos__cnt=CNTs.objects.get(id=2))
    usuarioInteru = userAll.filter(equiposdetrabajos__cnt=CNTs.objects.get(id=3))
    usuarioTellabs = userAll.filter(equiposdetrabajos__cnt=CNTs.objects.get(id=4))
    usuarioRadio = userAll.filter(equiposdetrabajos__cnt=CNTs.objects.get(id=7))
    usuarioSincro = userAll.filter(equiposdetrabajos__cnt=CNTs.objects.get(id=5))
    
    eventos = Evento.objects.filter(diaInicio__gt=datetime.datetime.now().date()-datetime.timedelta(days=30))
    
        
    eventosAcceso =  eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=1))
    eventosUrbano =  eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=2))
    eventosInteru =  eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=3))
    eventosTellabs =  eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=4))
    eventosRadio =  eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=7))
    eventoSincro = eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=5))
    
    #print(str(eventosAcceso.query))
    eventosGN = eventos.filter(tipoEvento='GUARDIA NOCHE')
    disponibilidades = eventos.filter(tipoEvento='DISPONIBILIDAD', profesional__is_supervisor=True)
    gn = []
    disp = []
    
    for e in eventosGN:
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
    
    onlineAcceso = panelAcceso.online()
    onlineUrbano = panelUrbano.online()
    onlineInteru = panelInteru.online()
    onlineTellabs = panelTellabs.online()
    onlineRadio = panelRadio.online()
    onlineSincro = panelSincro.online()
    """ for e in onlineTellabs:
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
    contexto= {'acceso':onlineAcceso,'urbano':onlineUrbano, 'interu': onlineInteru, 'tellabs':onlineTellabs, 'radio': onlineRadio, 'sincro':onlineSincro ,'noche': gn, 'disp':disp}
    #pequeño script para corregir horarios de salida
    """ for a in usuarioAcceso:
            a.save_horaSalida()
            
        for u in usuarioUrbano:
            u.save_horaSalida()
            
        for i in usuarioInteru:
            i.save_horaSalida()
    for u in usuarioTellabs:
        u.save_horaSalida()"""
    return render(request, 'publica/inicio-copy.html', context=contexto)