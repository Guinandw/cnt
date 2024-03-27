from datetime import timedelta, datetime, date, time
from django.db.models import Q
from cuentas.models import Usuarios as Profesionales, CNTs
from semana.models import Evento, Feriados

class Reportes:
    def __init__(self, fechaInicio, fechaFin):
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.feriados = Feriados.objects.all()
        self.dias = self.__dias__()

    def __dias__(self):
        dias = {}
        inicio = datetime.strptime(self.fechaInicio, "%Y-%m-%d" ).date()
        fin = datetime.strptime(self.fechaFin, "%Y-%m-%d").date()
        while inicio <= fin:
            dias[inicio.strftime('%d/%m')]= inicio
            inicio += timedelta(days=1)
        return dias
    
    def get_evento(self, profesional, dia):
        if Evento.objects.filter(Q(profesional=profesional) & Q(diaInicio__lte=dia) & Q(diaFin__gte=dia)).exists():
            return Evento.objects.get(Q(profesional=profesional) & Q(diaInicio__lte=dia) & Q(diaFin__gte=dia))
        else:
            return Evento(profesional=profesional, tipoEvento='NORMAL', diaInicio=date.today(), diaFin=date.today(), horaInicio=time(hour=profesional.preferenciaHorario, minute=00), duracion=profesional.horasXdia)

    def get_horario(self, evento_del_dia, dia, dia_str):
        horaFin = datetime(year=dia.year,month=dia.month,day=dia.day,hour=evento_del_dia.horaInicio.hour) + timedelta(hours=evento_del_dia.duracion)
        if str(dia) in [str(feriado.fecha) for feriado in self.feriados] or dia.weekday() in [5,6]:
            if evento_del_dia.tipoEvento in ['GUARDIA MAÑANA', 'GUARDIA TARDE']:
                return str(evento_del_dia.horaInicio.hour)+'a'+str(horaFin.hour)
            elif evento_del_dia.tipoEvento == 'GUARDIA NOCHE':
                return '23a7'
            else:
                return '/'
        else:
            if evento_del_dia.tipoEvento in ['GUARDIA MAÑANA', 'GUARDIA TARDE', 'DISPONIBILIDAD']:
                return str(evento_del_dia.horaInicio.hour)+'a'+str(horaFin.hour)
            elif evento_del_dia.tipoEvento in ['FRANCO', 'VACACIONES']:
                return evento_del_dia.tipoEvento[0]
            else:
                return str(profesional.preferenciaHorario)+'a'+str(profesional.horaFin)

    def eventos(self,filtro):
        prof = {}
        userAll = Profesionales.objects.all()
        profesionales = userAll.filter(equiposdetrabajos__cnt=CNTs.objects.get(id=filtro))
        for profesional in profesionales:
            prof[profesional.username]= {
                "nombreCompleto": profesional.first_name + ' ' + profesional.last_name,
                "telefono": profesional.telefono,
                "movil": profesional.movil
            }
            for key,dia in self.dias.items():
                evento_del_dia = self.get_evento(profesional, dia)
                horario = self.get_horario(evento_del_dia, dia, str(dia))
                prof[profesional.username][str(dia)]= horario
        return prof

    def supervision(self):
        prof={}
        if Evento.objects.filter(diaInicio__range=(self.fechaInicio, self.fechaFin), tipoEvento='DISPONIBILIDAD', profesional__is_supervisor=True).exists():
            disponibilidades = Evento.objects.filter(diaInicio__range=(self.fechaInicio, self.fechaFin), tipoEvento='DISPONIBILIDAD', profesional__is_supervisor=True)
            for d in disponibilidades:
                prof[d.profesional.username]= {
                    "Nombre": d.profesional.first_name + ' ' + d.profesional.last_name,
                    "Telefono": d.profesional.telefono,
                    "Movil": d.profesional.movil,
                    "Desde": d.diaInicio.strftime('%d/%m'),
                    "Hasta": d.diaFin.strftime('%d/%m')
                }
        return prof

    def guardiaNoche(self):
        prof={}
        if Evento.objects.filter(diaInicio__range=(self.fechaInicio, self.fechaFin), tipoEvento='GUARDIA NOCHE').exists():
            guardias_noche = Evento.objects.filter(diaInicio__range=(self.fechaInicio, self.fechaFin), tipoEvento='GUARDIA NOCHE')
            for d in guardias_noche:
                prof[d.profesional.username]= {
                    "Nombre": d.profesional.first_name + ' ' + d.profesional.last_name,
                    "Telefono": d.profesional.telefono,
                    "Movil": d.profesional.movil,
                    "Desde": d.diaInicio.strftime('%d/%m'),
                    "Hasta": d.diaFin.strftime('%d/%m')
                }
        return prof
