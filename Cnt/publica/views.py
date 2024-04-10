import datetime

from django.db.models import Q
from django.shortcuts import render
from django.http import request

from cuentas.models import Usuarios, CNTs
from semana.models import Evento, Feriados
from semana.semana import Panel
from cuentas import constantes as c
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
    usuarioSincro = userAll.filter(equiposdetrabajos__cnt=CNTs.objects.get(id=5))
    
    eventos = Evento.objects.filter(diaInicio__gt=datetime.datetime.now().date()-datetime.timedelta(days=30))
    
        
    eventosAcceso =  eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=c.ACCESO))
    eventosUrbano =  eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=c.URBANO))
    eventosInteru =  eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=c.INTERURBANO))
    eventosTellabs =  eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=c.TELLABS))
    eventosRadio =  eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=c.RADIO))
    eventoSincro = eventos.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=c.SINCRONISMO))
    
    eventosGN = eventos.filter(tipoEvento='GUARDIA NOCHE')
    disponibilidades = eventos.filter(tipoEvento='DISPONIBILIDAD', profesional__is_supervisor=True, profesional__equiposdetrabajos__cnt__in=[c.ACCESO,c.URBANO,c.INTERURBANO])
    radioRadio = eventosRadio.filter(tipoEvento='RADIO: RADIO', diaInicio__lte=datetime.datetime.now().date(), diaFin__gte=datetime.datetime.now().date())
    radioGestores = eventosRadio.filter(tipoEvento='RADIO: GESTORES', diaInicio__lte=datetime.datetime.now().date(), diaFin__gte=datetime.datetime.now().date())
    radioEscalamieneto =  eventosRadio.filter(tipoEvento='RADIO: ESCALAMIENTO', diaInicio__lte=datetime.datetime.now().date(), diaFin__gte=datetime.datetime.now().date())
    tellabsEscalamiento =  eventosTellabs.filter(tipoEvento='DISPONIBILIDAD', diaInicio__lte=datetime.datetime.now().date(), diaFin__gte=datetime.datetime.now().date()).last()
    
    
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
    panelSincro = Panel(eventoSincro, usuarioSincro, feriados)
    
    onlineAcceso = panelAcceso.online()
    onlineUrbano = panelUrbano.online()
    onlineInteru = panelInteru.online()
    onlineTellabs = panelTellabs.online()
    onlineSincro = panelSincro.online()
    
    
    contexto= {'acceso':onlineAcceso,'urbano':onlineUrbano, 'interu': onlineInteru,'eTellabs':tellabsEscalamiento , 'tellabs':onlineTellabs,
               'radioRadio': radioRadio, 'radioGestores': radioGestores, 'radioEscalamiento': radioEscalamieneto , 'sincro':onlineSincro ,'noche': gn, 'disp':disp}
    
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