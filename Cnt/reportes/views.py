import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .forms import ReportesForms
from cuentas.models import Usuarios, CNTs
from semana.models import Evento, Feriados
from semana.semana import Panel
from .reporte import Reportes, Test
# Create your views here.


@login_required
def reportesForm(request):
    reportesForm = ReportesForms(request.POST or None)
    contexto = { 'form':reportesForm}
    
    if request.method == 'GET':
        return render(request, template_name='reportes/reportes-form.html', context=contexto)
    else:
        if reportesForm.is_valid():
            inicio = reportesForm.cleaned_data['fechaInicio']
            fin = reportesForm.cleaned_data['fechaFin']
            #print(inicio)
            #print(fin)
            return redirect('reportes', fechaInicio=inicio, fechaFin=fin)
        else:
             messages.warning(request, reportesForm.errors)
             return render(request, template_name='reportes/reportes-form.html', context=contexto)

@login_required
def reportes(request, fechaInicio, fechaFin):
    
    reporte = Reportes(fechaInicio=fechaInicio, fechaFin=fechaFin)
    reporte.eventos()
  
    return redirect('inicio')

