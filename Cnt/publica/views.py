from django.shortcuts import render
from django.http import request
from cuentas.models import Usuarios, equiposDeTrabajos, CNTs, NOMBRES


# Create your views here.
def inicio(request):
    equipos = equiposDeTrabajos.objects.all()
    acceso = equipos.filter(cnt__nombre=1)
    urbano = equipos.filter(cnt__nombre=2)
    interurbano = equipos.filter(cnt__nombre=3)
    contexto= {'acceso':acceso,'urbano':urbano, 'interu': interurbano}
    #pequeño script para corregir horarios de salida
    """ for a in acceso:
        a.miembro.save_horaSalida()
        print(a.miembro.first_name)
        print(a.miembro.preferenciaHorario)
        print(a.miembro.horaSalida())
    for u in urbano:
        u.miembro.save_horaSalida()
    for i in interurbano:
        i.miembro.save_horaSalida() """
    return render(request, 'publica/inicio.html', context=contexto)