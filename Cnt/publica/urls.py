from django.urls.conf import path
from . import views

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
]
