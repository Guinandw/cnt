from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta

# Create your models here.

hoy = datetime.now()

NOMBRES = [
        (1, 'Acceso'),
        (2, 'Urbano'),
        (3,'Interurbano'),
        (4,'Tellabs'),
        (5, 'Radio'),
        (6,'Sincronismo'),
        (7, 'Soporte')
    ]

class Usuarios(AbstractUser):
    
    PREFERENCIAS = [
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10,'10'),
        (11,'11'),
        (12,'12'),
        (13,'13'),
        (14, '14'),
        
    ]
    
    HORASXDIA = [
        (7,'7'),
        (8,'8'),
        (9,'9'),
    ]
    
    email = models.EmailField( verbose_name='email', blank=False, unique=True)
    legajo = models.CharField(verbose_name='Legajo', max_length=6, blank=True, null=True)
    telefono = models.CharField(verbose_name='Telefono', max_length=10)
    movil = models.CharField(verbose_name='Movil', max_length=10)
    preferenciaHorario = models.IntegerField(verbose_name='Preferencia Horario',choices=PREFERENCIAS, default=2)
    horasXdia = models.IntegerField(verbose_name='Horas diarias',choices=HORASXDIA, default=1)
    is_supervisor= models.BooleanField(verbose_name='es_supervisor',default=False, blank=True, null=True)
    horaFin = models.IntegerField(verbose_name='Hora Salida', blank=True, null=True)
    def __str__(self):
        return f'{self.username}'
    
    def horaSalida(self):
            h =  datetime(year=hoy.year,month=hoy.month,day=hoy.day,hour=self.preferenciaHorario) + timedelta(hours=self.horasXdia)
            return h.hour
        
    def save_horaSalida(self):
        self.horaFin = self.horaSalida()
        super().save()

    class Meta:
        db_table = 'usuarios'
        managed = True
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios' 

class CNTs(models.Model):
    
    
    nombre = models.IntegerField(choices=NOMBRES, default=1)
    
    def __str__(self):
        return f"{NOMBRES[self.nombre-1][1]}" 
    
   
    
    class Meta:
        db_table = 'cnts'
        managed = True
        verbose_name = 'CNT'
        verbose_name_plural = 'CNTs'
         

class equiposDeTrabajos(models.Model):
    
    usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    cnt = models.ForeignKey(CNTs, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.cnt} {self.usuarios.first_name}'
    
    def __equipo__(self):
        return f'{self.cnt.nombre}'
    
    class Meta:
        db_table: 'equiposDeTrabajos'
        verbose_name = 'Equipo de Trabajo'
        verbose_name_plural = 'Equipos de Trabajos'