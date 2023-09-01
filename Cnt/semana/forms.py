from django import forms

class DateForm(forms.Form):
    inicio = forms.DateField()
    fin = forms.DateField()
    feriados = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    
    
    """ Se necesita comprobar varias cosas:
    Que la fecha inicio sea anterior a la fecha fin. En caso contrario debe enviar un mensaje indicando el error.
    Si hay feriados, se debe comprobar que el feriado esta dentro de la semana que se configuro.

    """

    """ def clean(self):
        cleaned_data = super().clean()
        inicio = cleaned_data.get("inicio")
        fin = cleaned_data.get("fin")
        
        if fin < inicio:
            msg = "La Fecha de Inicio debe ser anterior a la Fecha Fin"
            self.add_error('asunto', msg) """
        
        