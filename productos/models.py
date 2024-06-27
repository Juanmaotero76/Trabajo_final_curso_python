from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Motores(models.Model):
    combustible = models.CharField(max_length=20)
    cilindrada = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    fecha = models.DateField()
  
         
    def __str__(self):
        return f'{self.combustible} {self.cilindrada} {self.marca} {self.fecha}'
    
class Producto(models.Model):
    productoSeleccion = (
    ('motores','Motores'),
    ('radios', 'Radios'),
    ('aviones','Aviones'),
    ('otro', 'Otro'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    producto = models.CharField(max_length=15, choices=productoSeleccion, default='motores')
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)
    year = models.IntegerField() 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    telefonoContacto = models.IntegerField()
    emailContacto = models.EmailField()
    imagenproducto = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    class Meta:
        ordering = ['usuario', '-fechaPublicacion']

    def __str__(self):
        return self.titulo, self.precio
        #