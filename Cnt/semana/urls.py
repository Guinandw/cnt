from django.urls.conf import path
from . import views


urlpatterns = [
    path('cargarSemana/', views.cargarSemana, name='cargarSemana'),
    path('cargarFeriado/<sem>', views.cargarFeriado, name='cargarFeriado'),
    path('guardarSemana/<sem>', views.guardarSemana, name='guardarSemana'),
]