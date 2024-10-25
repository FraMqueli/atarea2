from django.urls import path 
from . import views


urlpatterns = [
    path('', views.portada, name='FraMqueli'),
    path('post', views.post, name='post'),
]
