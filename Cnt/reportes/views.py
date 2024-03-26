import tkinter as tk
from tkinter import filedialog



from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.template.loader import get_template
from weasyprint import HTML,CSS


from .forms import ReportesForms
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
def reportes(request, fechaInicio, fechaFin, bandera:int=None):
    
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
                'radio': radReporte, 'sincronismo': sinReporte, 'soporte': sopReporte, 'noche':noche, 'fechaInicio':fechaInicio, 'fechaFin':fechaFin }
    
    
    
    if bandera:
        seleccionar_ruta_destino(contexto=contexto)
    
    #HTML(string=html_template, base_url=request.build_absolute_uri()).write_pdf(stylesheets=[CSS(bootstrap),CSS(css_url)],encoding='utf-8')
    #return HttpResponse(pdf, content_type='application/pdf')
    return render(request, 'reportes/reportes.html', context=contexto)
    #return render(request, 'reportes/imprimirReportes.html', context=contexto)

def generar_pdf(contexto, ruta_destino):
    
    paper_width = '13in'
    paper_height = '8.5in'
    
    template = get_template('reportes/imprimirReportes.html')
    html_template = template.render(contexto)
    
    HTML(string=html_template).write_pdf(target=ruta_destino, presentational_hints=True, 
                                         stylesheets=[CSS(string='@page { size: %s %s; }' % (paper_width, paper_height))])

def seleccionar_ruta_destino(contexto):
    # Crear una ventana tkinter
    root = tk.Tk()
    root.title("Guardar PDF")
    
    # Obtener la ruta de destino del archivo PDF
    ruta_destino = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")])
    
    # Cerrar la ventana tkinter
    root.destroy()
    
    # Llamar a la función generar_pdf solo si se proporcionó una ruta_destino válida
    if ruta_destino:
        generar_pdf(contexto, ruta_destino)    