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

    def clean(self):
        cleaned_data = super().clean()
        dia_inicio = cleaned_data.get('fechaInicio')
        dia_fin = cleaned_data.get('fechaFin')
        
        if dia_fin < dia_inicio:
            msg = 'El dia de Inicio debe ser anterior al Dia Fin'
            self.add_error('fechaFin', msg)