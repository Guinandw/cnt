from django.urls.conf import path
from . import views


urlpatterns = [
   #path('cargar-evento/', views.evento, name='cargar-evento'),
   path('cargar-evento/<int:userId>', views.eventoId, name='cargar-evento'),
   path('lista-cargar-evento/', views.listaCargarEvento, name='lista-cargar-evento'),
   path('lista-de-eventos/<int:userId>', views.listaEvento, name='lista-evento'),
   path('eliminar-evento/<int:id>', views.eliminarEvento, name='eliminar-evento')
]