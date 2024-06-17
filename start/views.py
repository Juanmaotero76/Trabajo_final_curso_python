from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader

# Create your views here.
def inicio (request):
   
    return render(request, 'inicio/inicio.html')

def contacto (request):
    
    return render (request, 'inicio/contacto.html' )