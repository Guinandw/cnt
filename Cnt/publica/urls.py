from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
]
