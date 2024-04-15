from django.db import models
import datetime
from cuentas.models import Usuarios

# Create your models here.
class Evento(models.Model):
    
    #HOY = datetime.datetime.now()
    
    TIPO_EVENTO = [
        ('GUARDIA MAÑANA', 'GUARDIA MAÑANA'),
        ('GUARDIA TARDE', 'GUARDIA TARDE'),
        ('GUARDIA NOCHE', 'GUARDIA NOCHE'),
        ('DISPONIBILIDAD', 'DISPONIBILIDAD'),
        ('FRANCO', 'FRANCO'),
        ('VACACIONES', 'VACACIONES'),
        ('RADIO: RADIO', 'RADIO: RADIO'),
        ('RADIO: GESTORES', 'RADIO: GESTORES'),
        ('RADIO: ESCALAMIENTO', 'RADIO: ESCALAMIENTO')
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
        comienzoInicioJornada = datetime.datetime(year=self.diaInicio.year, month=self.diaInicio.month, day=self.diaInicio.day, hour=self.horaInicio.hour, minute=self.horaInicio.minute)
        return comienzoInicioJornada
    
    #devuelve un datetime.datetime con el dia y la hora del ultimo dia del evento
    def finRealdeEvento(self):
        finUltimaJornada = datetime.datetime(year=self.diaFin.year, month=self.diaFin.month, day=self.diaFin.day, hour=self.horaInicio.hour, minute=self.horaInicio.minute) + datetime.timedelta(hours=self.duracion)
        return finUltimaJornada
    
    #si el evento se encuentra en el dia de hoy, devolvera la fecha de hoy con la hora de salida. sino devolvera falso
    def finDeEventoHoy(self):
        if self.diaInicio <= datetime.datetime.now().date() and datetime.datetime.now().date() <= self.diaFin:
            comienzoJornadaHoy = datetime.datetime(year=datetime.datetime.now().year, month=datetime.datetime.now().month, day=datetime.datetime.now().day, hour=self.horaInicio.hour, minute=self.horaInicio.minute)
            finJornadaHoy = comienzoJornadaHoy + datetime.timedelta(hours=self.duracion)
            return finJornadaHoy
        else:
            return False
    #si el evento se encuentra en el dia de hoy, devolvera la fecha de hoy con la hora de entrada, sino devolvera falso  
    def inicioDeEventoHoy(self):
        #print(f'tipo {type(self.horaInicio)}, valor {self.horaInicio}')
        
        
        if self.diaInicio<= datetime.datetime.now().date() and datetime.datetime.now().date() <= self.diaFin:
            comienzoJornadaHoy = datetime.datetime(year=datetime.datetime.now().year, month=datetime.datetime.now().month, day=datetime.datetime.now().day, hour=self.horaInicio.hour, minute=self.horaInicio.minute)
            return comienzoJornadaHoy
        else:
            return False

    def evento_hoy(self):
         #DEVUELVE TRUE SI EL DIA DE HOY VA A OCURRIR EL EVENTO, ES PARECIDO A EVENTOS_HOY DE LA CLASE PANEL            
        if self.inicioRealdeEvento() <= datetime.datetime.now() and datetime.datetime.now() <= self.finRealdeEvento():
            return True
        else:
            return False 
               
    
    def username(self):
        return self.profesional.username
    

class Feriados(models.Model):
    
    fecha = models.DateField(
        verbose_name='Fecha'
    )
    
    def __str__(self):
       
        return self.fecha.strftime('%d/%m/%Y')
    
        