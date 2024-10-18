from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("<h1>Y weno 400 y deberías poder hacer esto</h1>")