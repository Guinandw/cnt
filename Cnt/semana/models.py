from django.db import models
import datetime
from cuentas.models import Usuarios

# Create your models here.

class Evento(models.Model):
    
    HOY = datetime.datetime.now()
    
    TIPO_EVENTO = [
        ('GUARDIA MAÑANA', 'GUARDIA MAÑANA'),
        ('GUARDIA TARDE', 'GUARDIA TARDE'),
        ('GUARDIA NOCHE', 'GUARDIA NOCHE'),
        ('DISPONIBILIDAD', 'DISPONIBILIDAD'),
        ('FRANCO', 'FRANCO'),
        ('VACACIONES', 'VACACIONES'),
    ]
    
    HORASXDIA = [
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (24,'24'),
    ]
    
    
    profesional = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    
    tipoEvento = models.CharField(
        verbose_name='Tipo de Evento',
        choices=TIPO_EVENTO,
        max_length=20
    )
    
    diaInicio = models.DateField(
        verbose_name='Dia Inicio del Evento',
        
    )
    diaFin = models.DateField(
        verbose_name='Dia Final Evento', 
    )
    horaInicio = models.TimeField(
        verbose_name='Hora Inicio'
    )
    
    duracion = models.IntegerField(
        verbose_name='Duracion',
        choices=HORASXDIA
    )
    
    def __str__(self):
        return f'{self.profesional.first_name} {self.tipoEvento} {self.diaInicio} {self.diaFin}'  
    
    #devuelve un datetime.datetime con el dia y la hora de inicio del evento
    def inicioRealdeEvento(self):
        comienzoInicioJornada = datetime.datetime(year=self.diaInicio.year, month=self.diaInicio.month, day=self.diaInicio.day, hour=self.__horaInicio.hour, minute=self.__horaInicio.minute)
        return comienzoInicioJornada
    
    def finRealdeEvento(self):
        finUltimaJornada = datetime.datetime(year=self.diaFin.year, month=self.diaFin.month, day=self.diaFin.day, hour=self.__horaInicio.hour, minute=self.__horaInicio.minute) + datetime.timedelta(hours=self.duracion)
        return finUltimaJornada
    
    def finDeEventoHoy(self):
        if self.diaInicio<= self.HOY.date() and self.HOY.date() <= self.diaFin:
            comienzoJornadaHoy = datetime.datetime(year=hoy.year, month=hoy.month, day=hoy.day, hour=self.__horaInicio.hour, minute=self.__horaInicio.minute)
            finJornadaHoy = comienzoJornadaHoy + datetime.timedelta(hours=self.duracion)
            return finJornadaHoy
        else:
            return False
        
    def inicioDeEventoHoy(self):
        if self.diaInicio<= self.HOY.date() and self.HOY.date() <= self.diaFin:
            comienzoJornadaHoy = datetime.datetime(year=self.HOY.year, month=self.HOY.month, day=self.HOY.day, hour=self.__horaInicio.hour, minute=self.__horaInicio.minute)
            return comienzoJornadaHoy
        else:
            return False
          

    def nombre(self):
        return self.profesional.first_name
    

class Feriados(models.Model):
    
    fecha = models.DateField(
        verbose_name='Fecha'
    )
    
    def __str__(self):
        strFecha = self.fecha.strftime('%d/%m/%Y')
        return self.fecha.strftime('%d/%m/%Y')
    
        