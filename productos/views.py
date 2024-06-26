from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Motores
from django.urls import reverse_lazy
 

class motores(ListView):
    model=Motores   
    template_name= 'motores/motores.html'  
    context_object_name = 'motores'  

class crearmotores(CreateView):
    model=Motores
    template_name= 'motores/crear_motores.html'  
    success_url=reverse_lazy('motores')
    fields=[ 'combustible', 'cilindrada','marca','fecha']  
    
    
class editarmotores(UpdateView):
    model=Motores
    template_name= 'motores/editar_motores.html'  
    success_url=reverse_lazy('motores')
    fields=[ 'combustible', 'cilindrada','marca','fecha']

class vermotores(DeleteView):
    model=Motores   
    template_name= 'motores/vermotores.html'
    
class eliminarmotores(DeleteView):
    model=Motores   
    template_name= 'motores/eliminar_motores.html'
    success_url=reverse_lazy('motores')
    


