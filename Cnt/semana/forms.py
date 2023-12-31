from django import forms
from .models import Evento
from cuentas.models import Usuarios

class EventoForm(forms.ModelForm):
    
    D = Usuarios.HORASXDIA 
    D.append((4,'24'))
    
    '''el profesional va a ser recibido directamente desde un parametro
    a la vista'''
    
    diaInicio=forms.DateField(
            label='Fecha Inicio', 
            widget=forms.DateInput(attrs={'class':'form-control','type':'date'})
        )
    
    diaFin=forms.DateField(
            label='Fecha Fin', 
            widget=forms.DateInput(attrs={'class':'form-control','type':'date'})
        )
    
    horaInicio=forms.TimeField(label='Hora Inicio',
                               widget=forms.TimeInput(attrs={'class':'form-control', 'type':'time'}))
    
    duracion=forms.CharField(
        label='Duración',
        initial='8',
        widget=forms.Select(choices=D, attrs={'class':'form-control'}),
        
    )
    
    
    class Meta:
        model = Evento
        fields = ['tipoEvento', 'diaInicio','diaFin', 'horaInicio', 'duracion']
        exclude = ['profesional']
        widget = {
            'tipoEvento': forms.TextInput(attrs={'class':'form-control'}),
            'diaInicio': forms.DateInput(attrs={'class':'','type':'date'})
        }
        
        
        
        
    """ Se necesita comprobar varias cosas:
    Que la fecha inicio sea anterior a la fecha fin. En caso contrario debe enviar un mensaje indicando el error.
    Si hay feriados, se debe comprobar que el feriado esta dentro de la semana que se configuro.

    """    
    
    def clean(self):
        cleaned_data = super().clean()
        dia_inicio = cleaned_data.get('diaInicio')
        dia_fin = cleaned_data.get('diaFin')
        
        if dia_fin < dia_inicio:
            msg = 'El dia de Inicio debe ser anterior al Dia Fin'
            self.add_error('diaFin', msg)
        



        
        