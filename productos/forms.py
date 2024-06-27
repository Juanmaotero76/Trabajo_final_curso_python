from django import forms
from django.contrib.auth.models import User
from productos.models import Producto

class FormularioNuevoProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('usuario', 'titulo', 'producto', 'marca', 'modelo', 'descripcion', 'year', 'precio', 'telefonoContacto', 'emailContacto', 'imagenproducto')

        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'producto' : forms.Select(attrs={'class': 'form-control'}),
            'marca' : forms.TextInput(attrs={'class': 'form-control'}),
            'modelo' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'year' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefonoContacto' : forms.TextInput(attrs={'class': 'form-control'}),
            'emailContacto' : forms.TextInput(attrs={'class': 'form-control'}),
        }
        

class EditarProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('titulo', 'producto', 'marca', 'modelo', 'descripcion', 'year', 'precio', 'telefonoContacto', 'emailContacto', 'imagenproducto')

        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'producto' : forms.Select(attrs={'class': 'form-control'}),
            'marca' : forms.TextInput(attrs={'class': 'form-control'}),
            'modelo' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'year' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefonoContacto' : forms.TextInput(attrs={'class': 'form-control'}),
            'emailContacto' : forms.TextInput(attrs={'class': 'form-control'}),
        }
