from django.urls import path 
from . import views

urlpatterns = [
    path('', views.hello, name='Inicio'),  # La URL base de esta app es accesible desde /framqueli/
]