from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from .forms import ReportesForms

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
            print(inicio)
            print(fin)
            return redirect('reportes', fechaInicio=inicio, fechaFin=fin)
    

@login_required
def reportes(request, fechaInicio, fechaFin):
    print(type(fechaInicio))
    print(type(fechaFin))
    return redirect('inicio')