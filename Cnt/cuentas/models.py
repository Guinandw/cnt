from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuarios(AbstractUser):
    
    PREFERENCIAS = [
        (1, '7'),
        (2, '8'),
        (3, '9'),
        (4,'10'),
        (5,'11'),
        (6,'12'),
        (7,'13'),
        (8, '14'),
        
    ]
    
    HORASXDIA = [
        (1,'7'),
        (2,'8'),
        (3,'9'),
    ]
    
    GUARDIA= [
        (1, 'Normal'),
        (2, 'Disponibilidad'),
        (3, 'Guardia Mañana'),
        (4, 'Guardia Tarde'),
        (5, 'Guardia Noche'),
    ]
    
    
    legajo = models.CharField(verbose_name='Legajo', max_length=6, blank=True, null=True)
    telefono = models.CharField(verbose_name='Telefono', max_length=10)
    movil = models.CharField(verbose_name='Movil', max_length=10)
    preferenciaHorario = models.IntegerField(verbose_name='Preferencia Horario',choices=PREFERENCIAS, default=2)
    horasXdia = models.IntegerField(verbose_name='Horas diarias',choices=HORASXDIA, default=1)
    guardia= models.IntegerField(verbose_name='guardia',choices=GUARDIA, default=1)
    is_supervisor= models.BooleanField(verbose_name='es_supervisor',default=False, blank=True, null=True)
    
    def __str__(self):
        return f'{self.username}'



    class Meta:
        db_table = 'usuarios'
        managed = True
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios' 

class CNTs(models.Model):
    NOMBRES = [
        (1, 'Acceso'),
        (2, 'Urbano'),
        (3,'Interurbano'),
        (4,'Tellabs'),
        (5, 'Radio'),
        (6,'Sincronismo'),
    ]
    
    nombre = models.IntegerField(choices=NOMBRES, default=1)
    
    def __str__(self):
        return f"{self.NOMBRES[self.nombre-1][1]}" 
    
   
    
    class Meta:
        db_table = 'cnts'
        managed = True
        verbose_name = 'CNT'
        verbose_name_plural = 'CNTs'
         

class equiposDeTrabajos(models.Model):
    
    miembro = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    cnt = models.ForeignKey(CNTs, on_delete=models.CASCADE)
    
    class Meta:
        db_table: 'equiposDeTrabajos'
        verbose_name = 'Equipo de Trabajo'
        verbose_name_plural = 'Equipos de Trabajos'