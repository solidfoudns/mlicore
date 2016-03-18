from django.db import models

# Create your models here.


class Provedor(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion


class Categoria(models.Model):
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.descripcion


class Articulo(models.Model):
    nombre = models.CharField(max_length=240)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria)
    provedor = models.ForeignKey(Provedor)
    precio_costo = models.DecimalField(decimal_places=2,max_digits=10)
    precio_venta = models.DecimalField(decimal_places=2,max_digits=10)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre