from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

def hello(request):
    # Genera la URL dinámica
    framqueli_url = reverse('FraMqueli')
    # Retorna el HTML con la URL generada
    return HttpResponse(f"""
        <h1>Esto es el incio, hay que adornarlo para describirnos y parecer pros</h1>
        <a href="{framqueli_url}">FraMqueli</a>
    """)
