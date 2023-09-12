from django.db import models
import datetime
# Create your models here.

class Semana(models.Model):
    primer = models.DateField(verbose_name='Primer')
    ultimo = models.DateField(verbose_name='Ultimo')
    detalles = models.JSONField(verbose_name='Detalles')
    
    def add_detalles(self):
        dias = []
        dia = self.primer
        while dia <= self.ultimo:
            if dia.weekday() in [5, 6]:
                valor = 'finDeSemana'
            else:
                valor = 'habil'
        dias.append({'dia': dia, 'valor': valor})
        dia += datetime.timedelta(days=1)
        return dias
        
    def agregar_feriado(self, d):
    #agrega un dia feria en la semana, faltaria saber como enviar un error si el feriado esta fuera de la 
    #semana en curso.
        for dia in self.detalles:
            if dia['dia']== d:
                dia['valor'] = 'feriado'
        super().save()