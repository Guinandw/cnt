import datetime

class Semanas:
  def __init__(self, inicio, fin):
    self.inicio = inicio
    self.fin = fin
    self.dias = self.obtener_dias()
    #self.feriados = []

  def obtener_dias(self):
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
  
  def agregar_feriado(self, d):
    #agrega un dia feria en la semana, faltaria saber como enviar un error si el feriado esta fuera de la 
    #semana en curso.
    dias = self.dias
    for dia in dias:
      if dia['dia']== d:
        dia['valor'] = 'feriado'
  
  
    