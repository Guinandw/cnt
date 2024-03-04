import datetime
from cuentas.models import Usuarios as Profesionales
from semana.models import Evento, Feriados


class Reportes:
    def __init__(self, fechaInicio, fechaFin):
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.profesionales = None
        self.eventos = Evento.objects.filter(diaInicio__range=(fechaInicio, fechaFin))
     