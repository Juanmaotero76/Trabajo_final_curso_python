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
 

class Motordetalle(DetailView):
    model = Producto
    context_object_name = 'motores'
    template_name = 'detalle.html'

class Motoreditar(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = EditarProducto
    success_url = reverse_lazy('motores')
    context_object_name = 'producto'
    template_name = 'editar.html'

class Eliminarmotor(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('motores')
    context_object_name = 'producto'
    template_name = 'borrar.html'

# aviones    
class Listadeaviones(ListView):
    context_object_name = 'aviones'
    queryset = Producto.objects.filter(producto__startswith='aviones')
    template_name = 'aviones/lista_de_aviones.html'
 

class Aviondetalle(DetailView):
    model = Producto
    context_object_name = 'aviones'
    template_name = 'detalle.html'

class Avioneditar(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = EditarProducto
    success_url = reverse_lazy('aviones')
    context_object_name = 'producto'
    template_name = 'editar.html'

class Eliminaravion(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('aviones')
    context_object_name = 'producto'
    template_name = 'borrar.html'
    
# radio    
class Listaderadios(ListView):
    context_object_name = 'radios'
    queryset = Producto.objects.filter(producto__startswith='radios')
    template_name = 'radios/lista_de_radios.html'
 

class Radiodetalle(DetailView):
    model = Producto
    context_object_name = 'radios'
    template_name = 'detalle.html'

class Radioditar(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = EditarProducto
    success_url = reverse_lazy('radios')
    context_object_name = 'producto'
    template_name = 'editar.html'

class Eliminarradio(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('radios')
    context_object_name = 'producto'
    template_name = 'borrar.html'

# otros    
class Listadeotros(ListView):
    context_object_name = 'otro'
    queryset = Producto.objects.filter(producto__startswith='otro')
    template_name = 'otros/lista_de_otros.html'
   

class Otrodetalle(DetailView):
    model = Producto
    context_object_name = 'otro'
    template_name = 'detalle.html'

class Otroeditar(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = EditarProducto
    success_url = reverse_lazy('otros')
    context_object_name = 'producto'
    template_name = 'editar.html'

class Eliminarotro(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('otros')
    context_object_name = 'producto'
    template_name = 'borrar.html'
     
def busquedaproducto(request):
    formulario=BuscarProducto(request.GET)
  
    if formulario.is_valid():
        tituloi=formulario.cleaned_data['Articulo']
        productoi=formulario.cleaned_data['Producto']
        productos=Producto.objects.filter(producto__icontains=productoi, titulo__icontains=tituloi)  
                 
        return render(request,'busqueda_producto.html',{'productos':productos, 'productoi':productoi, 'formulario':formulario})

 

# CREACION DE PRODUCTO

class crearproducto(CreateView):
    model = Producto
    form_class = FormularioNuevoProducto
    success_url = reverse_lazy('productos')
    template_name = 'crearproducto.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(crearproducto, self).form_valid(form)

