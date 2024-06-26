from django.db import models

# Create your models here.
class Motores(models.Model):
    combustible = models.CharField(max_length=20)
    cilindrada = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    fecha = models.DateField()
  
         
    def __str__(self):
        return f'{self.combustible} {self.cilindrada} {self.marca} {self.fecha}'
