from django.urls.conf import path
from . import views


urlpatterns = [
   path('cargar-evento/', views.evento, name='cargar-evento'),
]