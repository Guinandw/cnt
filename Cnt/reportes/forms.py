from django import forms

class ReportesForms(forms.Form):
    
    fechaInicio = forms.DateField(
        label='Fecha de Inicio',
        widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        
    )
    
    fechaFin = forms.DateField(
        label='Fecha Fin',
        widget=forms.DateInput(attrs={'class':'form-control' ,'type':'date'})
    )
