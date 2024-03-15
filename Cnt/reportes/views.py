import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .forms import ReportesForms
from cuentas.models import Usuarios, CNTs
from semana.models import Evento, Feriados
from semana.semana import Panel
from .reporte import Reportes, Test
from cuentas import constantes as c
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
    accReporte = reporte.eventos(c.ACCESO)
    urbReporte = reporte.eventos(c.URBANO)
    intReporte = reporte.eventos(c.INTERURBANO)
    telReporte = reporte.eventos(c.TELLABS)
    radReporte = reporte.eventos(c.RADIO)
    sinReporte = reporte.eventos(c.SINCRONISMO)
    sopReporte = reporte.eventos(c.SOPORTE)
    
    dias = reporte.__dias__()
    supervision = reporte.supervision()
    noche = reporte.guardiaNoche()
    contexto = {'dias': dias,'supervision':supervision, 'acceso':accReporte, 'urbano':urbReporte, 'interurbano': intReporte, 'tellabs': telReporte, 
                'radio': radReporte, 'sincronismo': sinReporte, 'soporte': sopReporte, 'noche':noche }
   
    return render(request, template_name='reportes/reportes.html', context=contexto)

