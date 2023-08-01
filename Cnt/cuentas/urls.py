from django.urls.conf import path
from . import views
urlpatterns = [
    path('login', views.login, name='login' )
]
