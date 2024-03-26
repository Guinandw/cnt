from django.urls.conf import path
from . import views

urlpatterns = [
    path('reportes-form/', views.reportesForm, name='reportes-form'),
    path('reportes/<str:fechaInicio>/<str:fechaFin>/', views.reportes, name='reportes'),
    path('reportes/<str:fechaInicio>/<str:fechaFin>/<int:bandera>', views.reportes, name='reportes'),
    
]
