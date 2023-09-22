from django.db import models
import datetime
from cuentas.models import Usuarios
# Create your models here.

class Evento(models.Model):
    
    TIPO_EVENTO = [
        ('GM', 'GUARDIA MAÑANA'),
        ('GT', 'GUARDIA TARDE'),
        ('GN', 'GUARDIA NOCHE'),
        ('DIS', 'DISPONIBILIDAD'),
        ('FRA', 'FRANCO'),
        ('VACA', 'VACACIONES'),
    ]
    
    profesional = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    
    tipoEvento = models.CharField(
        verbose_name='Tipo de Evento',
        choices=TIPO_EVENTO,
        max_length=4
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
        choices=Usuarios.HORASXDIA
    )
    
    
    

class Feriados(models.Model):
    
    fecha = models.DateField(
        verbose_name='Fecha'
    )
    
        