from django.urls.conf import path
from . import views
urlpatterns = [
    path('login', views.login, name='login' ),
    path('logout', views.salir, name='logout'),
    path('registro', views.crearCuentas, name='registro'),
    path('perfil', views.perfil, name='perfil'),
    path('cambiar_password', views.cambiar_password, name='cambiar_password'),
    path('editar_perfil', views.editar_perfil, name='editar_perfil'),
]
