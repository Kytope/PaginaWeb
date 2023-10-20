from django.db import models
from django.contrib.auth.models import User

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    fecha_reserva = models.DateField(default='2023-01-01')  

    def __str__(self):
        return f"Reserva de {self.usuario} para {self.fecha_hora}"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default='10')
    precio = models.PositiveIntegerField(default='100000') 
    descripcion = models.TextField(default='Descripcion del producto') 
    imagen = models.ImageField(upload_to='MiProyecto\static\productos', default='productos/default.jpg')