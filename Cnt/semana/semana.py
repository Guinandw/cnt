import datetime
from cuentas.models import Usuarios as Profesional
from .models import Evento

hoy = datetime.date.today()
ahora = datetime.datetime.now()

class Feriados:
    
    def __init__(self, fecha:datetime.date):
      self.fecha = fecha
    
    def __str__(self):
      return str(self.fecha)
    

  
""" class Profesional:
    def __init__(self, nombre, horasXdia:int, preferenciaEntrada:datetime.time):
        self.nombre = nombre
        self.horasXdia = horasXdia
        self.preferneciaEntrada = preferenciaEntrada

    def __str__(self):
        return f'{self.nombre}' """

    

""" class Evento:
    def __init__(self, profesional:Profesional, tipoEvento, diaInicio:datetime.date, diaFin: datetime.date = None, horaInicio:datetime.time = None, duracion:int = None):
      self.profesional = profesional
      self.tipoEvento = tipoEvento
      self.diaInicio = diaInicio
      self.diaFin = diaFin
      self.__horaInicio = horaInicio
      self.duracion = duracion
      
    
    def __str__(self):
        return f'{self.profesional.nombre} {self.tipoEvento} {self.diaInicio} {self.diaFin}'  
    
    #devuelve un datetime.datetime con el dia y la hora de inicio del evento
    def inicioRealdeEvento(self):
        comienzoInicioJornada = datetime.datetime(year=self.diaInicio.year, month=self.diaInicio.month, day=self.diaInicio.day, hour=self.__horaInicio.hour, minute=self.__horaInicio.minute)
        return comienzoInicioJornada
    
    def finRealdeEvento(self):
        finUltimaJornada = datetime.datetime(year=self.diaFin.year, month=self.diaFin.month, day=self.diaFin.day, hour=self.__horaInicio.hour, minute=self.__horaInicio.minute) + datetime.timedelta(hours=self.duracion)
        return finUltimaJornada
    
    def finDeEventoHoy(self):
        if self.diaInicio<= hoy and hoy <= self.diaFin:
            comienzoJornadaHoy = datetime.datetime(year=hoy.year, month=hoy.month, day=hoy.day, hour=self.__horaInicio.hour, minute=self.__horaInicio.minute)
            finJornadaHoy = comienzoJornadaHoy + datetime.timedelta(hours=self.duracion)
            return finJornadaHoy
        else:
            return False
        
    def inicioDeEventoHoy(self):
        if self.diaInicio<= hoy and hoy <= self.diaFin:
            comienzoJornadaHoy = datetime.datetime(year=hoy.year, month=hoy.month, day=hoy.day, hour=self.__horaInicio.hour, minute=self.__horaInicio.minute)
            return comienzoJornadaHoy
        else:
            return False
          

    def nombre(self):
        return self.profesional.nombre
     """
   

       
      
class Panel:
    def __init__(self, eventos:list[Evento], profesionales:list[Profesional], feriados:list[Feriados]):
        self.eventos = eventos
        self.profesionales = profesionales
        self.feriados = feriados
        '''el panel debe machear todos los eventos que hay para todos los profesionales. Si el profesional no tiene nigun evento, debera trabajar en su horario
        normal de trabajo, en caso de haber algun evento (guardia/disponibilidad/franco/vacaciones)'''
        
    #esta funcion debera devolver una lista de quienes trabajan hoy y el horario en la que trabajan., y no si estan online o no.
    def hoy_trabajan(self):
        en_linea = []
        #es hoy un feriado?
        hoy = datetime.date.today()
        if str(hoy) in [str(feriado.fecha) for feriado in self.feriados]:
            #Hoy es un dia feriado: solo trabajan los que estan de guardia, en el horario correspondiente. Se debe verificar la lista de eventos del dia
            #de hoy. Disponibilidad trabaja pero no esta online!
            print('Hoy es feriado')
            en_linea = self.eventos_hoy(['guardia'])
            
        #elif: ESTOY HOY FIN DE SEMANA?
        elif hoy.weekday() in [5,6]:
            print('Es Fin de semana')
            en_linea = self.eventos_hoy(['guardia'])
        else:
            #Hoy es un dia Habil: trabajan todos menos quienes esten de franco/Vacaciones, 
            # se cambian el horario de conexion para quienes esten de guardia/disponibilidad
            print('Hoy es un dia Habil')
            en_linea = self.eventos_hoy(['guardia', 'disponibilidad'])
            francos = self.eventos_hoy(['franco'])
            
            for profesional in self.profesionales:
                #verificando quien esta de franco
                if profesional.nombre in [franco.nombre() for franco in francos]:
                    pass
                else:
                    if profesional.nombre in [guardia.nombre() for guardia in en_linea]:
                        pass
                    else:
                        print(profesional.horasXdia)
                        en_linea.append(Evento(profesional=profesional, tipoEvento='normal', diaInicio=hoy, diaFin=hoy, horaInicio=profesional.preferneciaEntrada, duracion=profesional.horasXdia))
                    #esta es la lista de los profesionales que no tienen franco, los que no tienen guardia se creara un evento con el horario normal.
                    
                
        return en_linea        

            
            
      
    def eventos_hoy(self, filtro:list[str]=None):
        #va a verificar si en el dia de hoy hay algun evento. Siempre que la fecha de hoy este dentro de la fecha inicio y fin de un evento, se va a agregar
        #a la lista de eventos
        lista = []
        for evento in self.eventos:
            if evento.inicioRealdeEvento() <= datetime.datetime.now().date() and datetime.datetime.now().date() <= evento.finRealdeEvento():
                if filtro == None:
                    lista.append(evento)
                else:
                    if evento.tipoEvento in filtro:
                        lista.append(evento)
        return lista

    
 
  

""" 
will = Profesional('willian', 7, datetime.time(8,0))
max = Profesional('Max', 7, datetime.time(8,0))
rober = Profesional('Robert',9,datetime.time(10,0))
mati = Profesional('Mati', 9, datetime.time(8,0))
nimo = Profesional('Nimo', 7, datetime.time(12,0))
listaProfesionales = [will, max, rober, mati, nimo]

g_will = Evento(will, 'disponibilidad', datetime.date(2023,9,11), datetime.date(2023,9,17), datetime.time(12,0), 7)
d_mati = Evento(mati, 'disponibilidad', datetime.date(2023,9,4), datetime.date(2023,9,10), datetime.time(12,0),mati.horasXdia)
g_robert = Evento(rober, 'guardia', datetime.date(2023,9,11), datetime.date(2023,9,17), datetime.time(15,0), 8)
f_maxi = Evento(max, 'franco',datetime.date(2023,9,7), datetime.date(2023,9,7),)
#nimo horario normal
print('Evento Guardia Willy ' + str(g_will.finRealdeEvento()))
listaEventos = [g_will, d_mati, g_robert,f_maxi]

v7_9 = Feriados(datetime.date(2023,9,7))
v8_9 = Feriados(datetime.date(2023,9,8))
v9_9 = Feriados(datetime.date(2023,9,9))
listaFeriados = [v7_9, v9_9]


panel = Panel(listaEventos, listaProfesionales, listaFeriados)

 """

""" print(datetime.datetime.now().date())
print(datetime.datetime.now().date() in listaFeriados)"""


""" online = panel.hoy_trabajan()

for o in online:
    print(o)
    print('hora inicio: ' + str(o.inicioDeEventoHoy()))
    print('Duracion' + str(o.duracion))
    print('Hora fin' + str(o.finDeEventoHoy()))
    if o.inicioDeEventoHoy() <= ahora and ahora <= o.finDeEventoHoy():
        print('ONLINE')
    else:
        print('OFFLINE')
    print('\n') """