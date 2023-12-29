import datetime
from cuentas.models import Usuarios as Profesional
from .models import Evento



class Feriados:
    
    def __init__(self, fecha:datetime.date):
      self.fecha = fecha
    
    def __str__(self):
      return str(self.fecha)
    

       
      
class Panel:
    def __init__(self, eventos:list[Evento], profesionales:list[Profesional], feriados:list[Feriados]):
        self.eventos = eventos
        self.profesionales = profesionales
        self.feriados = feriados
        '''el panel debe machear todos los eventos que hay para todos los profesionales. Si el profesional 
        no tiene nigun evento, debera trabajar en su horario
        normal de trabajo, en caso de haber algun evento (guardia/disponibilidad/franco/vacaciones)'''
        
    #esta funcion debera devolver una lista de TODOS los que trabajan hoy y el horario en la que trabajan., Y NO! SI ESTAN ONLINE O NO.
    def hoy_trabajan(self):
        en_linea = None

        #es hoy un feriado?
        if str(datetime.date.today()) in [str(feriado.fecha) for feriado in self.feriados]:
            #Hoy es un dia feriado: solo trabajan los que estan de guardia, en el horario correspondiente. Se debe verificar la lista de eventos del dia
            #de hoy. Disponibilidad trabaja pero no esta online!
            print('Hoy es feriado')
            en_linea = self.eventos_hoy(['GUARDIA'])
            
        #elif: ESTOY HOY FIN DE SEMANA? SOLO TRABAJAN LOS QUE ESTAN DE GUARDIA
        elif datetime.date.today().weekday() in [5,6]:
            print('Es Fin de semana')
            en_linea = self.eventos_hoy(['GUARDIA'])
        else:
            #Hoy es un dia Habil: trabajan todos menos quienes esten de franco/Vacaciones, 
            # se cambian el horario de conexion para quienes esten de guardia/disponibilidad
            print('Hoy es un dia Habil')
            #EN_LINEA Y FRANCOS SON DOS LISTAS DE EVENTOS
            en_linea = self.eventos_hoy(['GUARDIA', 'DISPONIBILIDAD'])
            francos = self.eventos_hoy(['FRANCO', 'VACACIONES'])
            
            for profesional in self.profesionales:
                
                #verificando quien esta de franco
                if profesional.username in [franco.username() for franco in francos]:
                    pass
                else:
                    
                    if profesional.username in [guardia.username() for guardia in en_linea]:
                        #GUARDIA ACA
                        pass
                    else:
                        en_linea.append(Evento(profesional=profesional, tipoEvento='normal', diaInicio=datetime.date.today(), diaFin=datetime.date.today(), horaInicio=datetime.time(hour=profesional.preferenciaHorario, minute=00), duracion=profesional.horasXdia))
                    #esta es la lista de los profesionales que no tienen franco, los que no tienen guardia se creara un evento con el horario normal.
                    
        #regresa una lista de los que trabajan hoy        
        return en_linea        

    
            
            
      
    def eventos_hoy(self, filtro:list[str]=None):
        #va a verificar si en el dia de hoy hay algun evento. Siempre que la fecha de hoy este dentro de la fecha inicio y fin de un evento, se va a agregar
        #a la lista de eventos
        lista = []
        for evento in self.eventos:
            #primero evaluamos si estamos dentro de la FECHA (.date()) inicio y fin reales del evento, sino no lo tomamos en cuenta
            #porque que es un evento pasado o futuro. 
            #No interesan la hora exacta, solo si esta dentro del dia
            if evento.inicioRealdeEvento().date() <= datetime.datetime.now().date() and datetime.datetime.now().date() <= evento.finRealdeEvento().date():
                
                #si no hay ningun filtro se agregan todos los eventos
                if filtro == None:
                    lista.append(evento)
                else:
                    #se agrega a la lista solo los eventos que corresponde al filtro.
                    for i in filtro:
                        if i in evento.tipoEvento:
                            lista.append(evento)
        return lista

    #EVALUA DE LA LISTA EXTRAIDA DE LA FUNCION HOY_TRABAJAN, SI ESTAN ONLINE O NO.
    def online(self):
        conectados = []
        lista = self.hoy_trabajan()
        
        for e in lista:
            '''print(f'-----------')
            print(f'{e.tipoEvento}')
            print(e.inicioDeEventoHoy())
            print(datetime.datetime.now().replace(minute=0, second=0, microsecond=0))
            print(e.finDeEventoHoy())'''
            if not e.inicioDeEventoHoy() or not e.finDeEventoHoy():
                pass
            else:
                if e.inicioDeEventoHoy() <= datetime.datetime.now() and datetime.datetime.now() <= e.finDeEventoHoy():
                    conectados.append(e)
                    #print(f'{e.profesional.username}: ONLINE')
                    #print(f'{e.tipoEvento}')
                else:
                    #print(f'{e.profesional.username}: OFFLINE')
                                      
                    pass
                    

        return conectados
