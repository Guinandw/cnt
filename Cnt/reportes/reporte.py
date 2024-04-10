
from datetime import timedelta, datetime, date, time

from django.db.models import Q
from cuentas.models import Usuarios as Profesionales, CNTs
from cuentas import constantes as c
from semana.models import Evento, Feriados
from cuentas import constantes as c

''' 
-INGRESA FECHA INICIO Y FECHA FIN 
-CREA TODAS LAS FECHAS DENTRO DE ESE RANGO EN UN DICCIONARIO
-EVALUA PARA CADA FECHA DENTRO DEL RANGO SI HAY UN EVENTO PARA CADA PROFESIONAL
-SI HAY EVENTO VERIFICA LA HORA DE INICIO Y DURACION, EN CASO DE SER FRANCO O VACACICONES DEBERA COLOCAR UNA 'F' O UNA 'V'
-SI NO HAY EVENTOS DEBERA EXTRAER DEL PERFIL DEL PROFESIONAL LA HORA DE PREFERENCIA DE ENTRADA Y LA HORA FIN.

ESTA CLASE DEBERA DEVOLVER UN DICCIONARIO CON TODA LA INFO SUFICIENTE PARA CREAR UNA TABLA Y TODO EL CONTENIDO DE ELLA

'''

class Reportes:
    def __init__(self, fechaInicio, fechaFin):
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.feriados = Feriados.objects.all()
        self.dias = self.__dias__()
        self.userAll = Profesionales.objects.all()
        #OJO: QUE PASA SI NO HAY NINGUN EVENTO?
        
    
    
    #crea un array con todos los dias que va a tener el reporte.
    def __dias__(self):
        dias = {}
        inicio = datetime.strptime(self.fechaInicio, "%Y-%m-%d" ).date()
        fin = datetime.strptime(self.fechaFin, "%Y-%m-%d").date()
        
        while inicio <= fin:
            #print(inicio)
            dias[inicio.strftime('%d/%m')]= inicio
            inicio += timedelta(days=1)
        return dias
    
    def __get_titulo__(self):
        inicio = datetime.strptime(self.fechaInicio, "%Y-%m-%d" ).date()
        fin = datetime.strptime(self.fechaFin, "%Y-%m-%d").date()
        
        return 'Reporte del '+ inicio.strftime("%d/%m") + ' al ' + fin.strftime("%d/%m")
        
    
    def __get_evento__(self, profesional, dia):
        #Hay evento para este dia? verificamos si existe primero
                
        if Evento.objects.filter(Q(profesional=profesional) & Q(diaInicio__lte=dia) & Q(diaFin__gte=dia)).exists():
            #Y si existe lo obtengo
            return Evento.objects.get(Q(profesional=profesional) & Q(diaInicio__lte=dia) & Q(diaFin__gte=dia))
        else:
            return Evento(profesional=profesional, tipoEvento='NORMAL', diaInicio=date.today(), diaFin=date.today(), horaInicio=time(hour=profesional.preferenciaHorario, minute=00), duracion=profesional.horasXdia)
    
    def __get_horario__(self, evento_del_dia, dia):
        horaFin = datetime(year=dia.year,month=dia.month,day=dia.day,hour=evento_del_dia.horaInicio.hour) + timedelta(hours=evento_del_dia.duracion)
        if str(dia) in [str(feriado.fecha) for feriado in self.feriados] or dia.weekday() in [5,6]:
            if evento_del_dia.tipoEvento in ['GUARDIA MAÑANA', 'GUARDIA TARDE']:
                return str(evento_del_dia.horaInicio.hour)+'a'+str(horaFin.hour)
            elif evento_del_dia.tipoEvento == 'GUARDIA NOCHE':
                return '23a7'
            else:
                return '/'
        else:
            if evento_del_dia.tipoEvento in ['GUARDIA MAÑANA', 'GUARDIA TARDE','GUARDIA NOCHE', 'DISPONIBILIDAD']:
                return str(evento_del_dia.horaInicio.hour)+'a'+str(horaFin.hour)
            elif evento_del_dia.tipoEvento in ['FRANCO', 'VACACIONES']:
                return evento_del_dia.tipoEvento[0]
            else:
                return str(evento_del_dia.profesional.preferenciaHorario)+'a'+str(evento_del_dia.profesional.horaFin)

    
    def eventos(self,filtro):
        prof = {}
    
        profesionales = self.userAll.filter(equiposdetrabajos__cnt=CNTs.objects.get(id=filtro))
             
        for profesional in profesionales:
            prof[profesional.username]= {}
            prof[profesional.username]["nombreCompleto"]=profesional.first_name + ' ' + profesional.last_name
            prof[profesional.username]["telefono"]= profesional.telefono
            prof[profesional.username]["movil"]=profesional.movil
                
            for key,dia in self.dias.items():
                #dia es un datetime.date
                
                evento_del_dia = self.__get_evento__(profesional,dia)
                horario = self.__get_horario__(evento_del_dia, dia)
                prof[profesional.username][str(dia)]=horario   
        

        #print(prof)
        return prof

    def supervision(self):
        prof={}
        if Evento.objects.filter(diaInicio__range=(self.fechaInicio, self.fechaFin)).exists():
            eventos = Evento.objects.filter(diaInicio__range=(self.fechaInicio, self.fechaFin))
            if eventos.filter(tipoEvento='DISPONIBILIDAD', profesional__is_supervisor=True).exists():
                disponibilidades = eventos.filter(tipoEvento='DISPONIBILIDAD', profesional__is_supervisor=True)
                
                for d in disponibilidades:
                    prof[d.profesional.username]= {}
                    prof[d.profesional.username]["Nombre"]=d.profesional.first_name + ' ' + d.profesional.last_name
                    prof[d.profesional.username]["Telefono"]= d.profesional.telefono
                    prof[d.profesional.username]["Movil"]=d.profesional.movil
                    prof[d.profesional.username]["Desde"]=d.diaInicio.strftime('%d/%m')
                    prof[d.profesional.username]["Hasta"]=d.diaFin.strftime('%d/%m')
            else:
                prof = None
        return prof
    
    def guardiaNoche(self):
        #como la guardia noche siempre comienza un dia antes que cualquier guardia, se tuvo que crear la variable diaInicio para la noche
        diaInicioNocturno =  datetime.strptime(self.fechaInicio, "%Y-%m-%d" ).date() - timedelta(days=1)
        diaFinNocturno = datetime.strptime(self.fechaFin, "%Y-%m-%d" ).date() - timedelta(days=1)
        prof={}
        if Evento.objects.filter(diaInicio__range=(diaInicioNocturno, diaFinNocturno)).exists():
            eventos = Evento.objects.filter(diaInicio__range=(diaInicioNocturno, diaFinNocturno))
            if eventos.filter(tipoEvento='GUARDIA NOCHE').exists():
                disponibilidades = eventos.filter(tipoEvento='GUARDIA NOCHE')
                
                for d in disponibilidades:
                    prof[d.profesional.username]= {}
                    prof[d.profesional.username]["Nombre"]=d.profesional.first_name + ' ' + d.profesional.last_name
                    prof[d.profesional.username]["Telefono"]= d.profesional.telefono
                    prof[d.profesional.username]["Movil"]=d.profesional.movil
                    prof[d.profesional.username]["Desde"]=d.diaInicio.strftime('%d/%m')
                    prof[d.profesional.username]["Hasta"]=d.diaFin.strftime('%d/%m')
            else:
                prof = None
        return prof

    def dispTellabs(self):
        eventosTellabs =  Evento.objects.filter(profesional__equiposdetrabajos__cnt=CNTs.objects.get(id=4))
        eventosTellabs = eventosTellabs.filter(Q(diaInicio__lte=self.fechaInicio) & Q(diaFin__gte=self.fechaFin))
        if eventosTellabs.filter(tipoEvento='DISPONIBILIDAD').exists():
            disp = eventosTellabs.filter(tipoEvento='DISPONIBILIDAD').last()        
        else:
            disp = None
        return disp    
    
    def __getEventFilter__(self, tipoEvento:str, deltaTime:int, supervision:bool=None, cnts_a_buscar=[]):
        diaInicioNocturno =  datetime.strptime(self.fechaInicio, "%Y-%m-%d" ).date() - timedelta(days=deltaTime)
        diaFinNocturno = datetime.strptime(self.fechaFin, "%Y-%m-%d" ).date() - timedelta(days=deltaTime)
        prof={}
        if Evento.objects.filter(diaInicio__range=(diaInicioNocturno, diaFinNocturno), profesional__equiposdetrabajos__cnt__in=cnts_a_buscar).exists():
            eventos = Evento.objects.filter(diaInicio__range=(diaInicioNocturno, diaFinNocturno), profesional__equiposdetrabajos__cnt__in=cnts_a_buscar)
            if eventos.filter(tipoEvento=tipoEvento).exists():
                if supervision is None:
                    disponibilidades = eventos.filter(tipoEvento=tipoEvento)
                else:
                    disponibilidades = eventos.filter(tipoEvento=tipoEvento, profesional__is_supervisor=supervision)

            
                
                for d in disponibilidades:
                    prof[d.profesional.username]= {}
                    prof[d.profesional.username]["Nombre"]=d.profesional.first_name + ' ' + d.profesional.last_name
                    prof[d.profesional.username]["Telefono"]= d.profesional.telefono
                    prof[d.profesional.username]["Movil"]=d.profesional.movil
                    prof[d.profesional.username]["Desde"]=d.diaInicio.strftime('%d/%m')
                    prof[d.profesional.username]["Hasta"]=d.diaFin.strftime('%d/%m')
            else:
                prof = None
        return prof
    
    
       
class Test:
    def __init__(self):
        self.fechaInicio = None
        self.fechaFin = None
        self.feriados = Feriados.objects.all()
    
    def prueba(self):
        dia = date(year=2024,month=3,day=13)
        profesional = Profesionales.objects.get(username='defelicea')
        print(profesional.first_name)
        evento_tester = Evento.objects.get(Q(profesional=profesional) & Q(diaInicio__lte=dia) & Q(diaFin__gte=dia)  )
        
        print(evento_tester)
        print(evento_tester.horaInicio.hour)
        print(type(evento_tester.horaInicio.hour))
        