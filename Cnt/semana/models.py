from django.db import models
import datetime
# Create your models here.

class Semana(models.Model):
    primer = models.DateField(verbose_name='Primer')
    ultimo = models.DateField(verbose_name='Ultimo')
    detalles = models.JSONField(verbose_name='Detalles')
    
    def save(self):
        dias = []
        dia = self.inicio
        while dia <= self.fin:
            if dia.weekday() in [5, 6]:
                valor = 'finDeSemana'
            else:
                valor = 'habil'
        dias.append({'dia': dia, 'valor': valor})
        dia += datetime.timedelta(days=1)
        return dias
        super().save()
        
        