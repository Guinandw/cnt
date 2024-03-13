
from datetime import timedelta, datetime, date, time

from django.db.models import Q
from cuentas.models import Usuarios as Profesionales
from cuentas import constantes as c
from semana.models import Evento, Feriados

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
        
        #OJO: QUE PASA SI NO HAY NINGUN EVENTO?
        
    
    
    #crea un array con todos los dias que va a tener el reporte.
    def __dias__(self):
        dias = {}
        inicio = datetime.strptime(self.fechaInicio, "%Y-%m-%d" ).date()
        fin = datetime.strptime(self.fechaFin, "%Y-%m-%d").date()
        
        while inicio <= fin:
            #print(inicio)
            dias[inicio.strftime('%Y-%m-%d')]= inicio
            inicio += timedelta(days=1)
        return dias
    
    def eventos(self):
        prof = {}
        profesionales = Profesionales.objects.exclude(equiposdetrabajos__isnull=True)
        eventos = Evento.objects.filter(diaInicio__range=(self.fechaInicio, self.fechaFin))
        
        dias = self.__dias__()
        for profesional in profesionales:
            prof[profesional.username]= {}
            prof[profesional.username]["nombreCompleto"]=profesional.first_name + ' ' + profesional.last_name
            prof[profesional.username]["telefono"]= profesional.telefono
            prof[profesional.username]["movil"]=profesional.movil
                
            for key,dia in dias.items():
                #dia es un datetime.date
                
                #Hay evento para este dia? verificamos si existe primero
                #Y si existe lo obtengo
                if Evento.objects.filter(Q(profesional=profesional) & Q(diaInicio__lte=dia) & Q(diaFin__gte=dia)).exists():
                    evento_del_dia = Evento.objects.get(Q(profesional=profesional) & Q(diaInicio__lte=dia) & Q(diaFin__gte=dia))
                else:
                    evento_del_dia = Evento(profesional=profesional, tipoEvento='NORMAL', diaInicio=date.today(), diaFin=date.today(), horaInicio=time(hour=profesional.preferenciaHorario, minute=00), duracion=profesional.horasXdia)
                
                
                horaFin = datetime(year=dia.year,month=dia.month,day=dia.day,hour=evento_del_dia.horaInicio.hour) + timedelta(hours=evento_del_dia.duracion)
                
                
                #verificamos si el dia es feriado o fin de semana
                if str(dia) in [str(feriado.fecha) for feriado in self.feriados] or dia.weekday() in [5,6] :
                       
                    if evento_del_dia.tipoEvento in ['GUARDIA MAÑANA', 'GUARDIA TARDE']:
                        horario = str(evento_del_dia.horaInicio.hour)+'a'+str(horaFin.hour)
                    elif evento_del_dia.tipoEvento in ['GUARDIA NOCHE']:
                        horario = '23a7'
                    else:
                        horario = '/'
                else:
                    if evento_del_dia.tipoEvento in ['GUARDIA MAÑANA', 'GUARDIA TARDE']:
                        horario = str(evento_del_dia.horaInicio.hour)+'a'+str(horaFin.hour)
                    elif evento_del_dia.tipoEvento in ['GUARDIA NOCHE']:
                        horario = '23a7'
                    elif evento_del_dia.tipoEvento in ['DISPONIBILIDAD']:
                        horario = str(evento_del_dia.horaInicio.hour)+'a'+str(horaFin.hour)
                    elif evento_del_dia.tipoEvento in ['FRANCO']:
                        horario = 'F'
                    elif evento_del_dia.tipoEvento in ['VACACIONES']:
                        horario = 'V'
                    else:
                        #por ultimo es el caso que no hay eventos, entonces el horario es su horario del perfil.
                        horario = str(profesional.preferenciaHorario)+'a'+str(profesional.horaFin)
                                   
                prof[profesional.username][str(dia)]=horario   

        for key, value in prof.items():
            print("clave:", key)
            for key, v in value.items():
                print("clave:", key)
                print("valor:", v)
                print("------")
        
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
        