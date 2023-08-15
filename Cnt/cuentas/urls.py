from django.urls.conf import path
from . import views
urlpatterns = [
    path('login', views.login, name='login' ),
    path('logout', views.salir, name='logout'),
    path('registro', views.crearCuentas, name='registro'),
    path('perfil', views.perfil, name='perfil'),    
]
