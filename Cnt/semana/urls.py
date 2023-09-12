from django.urls.conf import path
from . import views


urlpatterns = [
    path('cargarSemana/', views.cargarSemana, name='cargarSemana'),
    path('cargarFeriado/<int:sem>', views.cargarFeriado, name='cargarFeriado'),
    path('guardarSemana/', views.guardarSemana, name='guardarSemana'),
]