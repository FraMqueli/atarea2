from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def portada(request):
    return HttpResponse("<h1>Esto es la portada de Framqueli aquí jugaré con mis ramos, habilidades y etc.</h1>")