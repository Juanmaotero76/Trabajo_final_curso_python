from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Motores, Producto
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import FormularioNuevoProducto, EditarProducto, BuscarProducto
from django.template import Template, Context, loader
def productos (request):
    return render (request, 'productos.html' )
  

# Motores
class Listademotores(ListView):
    context_object_name = 'motores'
    queryset = Producto.objects.filter(producto__startswith='motores')
    template_name = 'motores/lista_de_motores.html'
    login_url = '/loguin/'

class Motordetalle(DetailView):
    model = Producto
    context_object_name = 'motores'
    template_name = 'motores/detalle_motor.html'

class Motoreditar(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = EditarProducto
    success_url = reverse_lazy('motores')
    context_object_name = 'motores'
    template_name = 'motores/editar_motores.html'

class Eliminarmotor(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('motores')
    context_object_name = 'motores'
    template_name = 'motores/borrar_motor.html'

# aviones    
class Listadeaviones(ListView):
    context_object_name = 'aviones'
    queryset = Producto.objects.filter(producto__startswith='aviones')
    template_name = 'aviones/lista_de_aviones.html'
    login_url = '/loguin/'

class Aviondetalle(LoginRequiredMixin, DetailView):
    model = Producto
    context_object_name = 'aviones'
    template_name = 'aviones/detalle_avion.html'

class Avioneditar(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = EditarProducto
    success_url = reverse_lazy('aviones')
    context_object_name = 'aviones'
    template_name = 'aviones/editar_avion.html'

class Eliminaravion(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('aviones')
    context_object_name = 'aviones'
    template_name = 'aviones/borrar_avion.html'
     
def busquedaproducto(request):
    formulario=BuscarProducto(request.GET)
  
    if formulario.is_valid():
        tituloi=formulario.cleaned_data['Articulo']
        productos=Producto.objects.filter(titulo__icontains=tituloi)  
         
        return render(request,'motores/busqueda_producto.html',{'productos':productos, 'formulario':formulario})

 

# CREACION DE PRODUCTO

class crearproducto(CreateView):
    model = Producto
    form_class = FormularioNuevoProducto
    success_url = reverse_lazy('productos')
    template_name = 'crearproducto.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(crearproducto, self).form_valid(form)

