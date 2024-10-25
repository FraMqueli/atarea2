from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Project

def portada(request):
    project = Project.objects.all()
    return render(request, 'home.html', {'project': project})

def post(request):
    return render(request, 'post.html')