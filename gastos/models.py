from django.db import models

# Create your models here.


class TipoGasto(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Gasto(models.Model):
    tipo_gasto = models.ForeignKey(TipoGasto
                                   )
    costo = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self):
        return self.tipo_gasto


UM_CHOICES = (
    ('sn', 'Sin Unidad de Medida '),
    ('pza', 'Pieza'),
    ('pqt', 'Paquete',)
)


class Insumo(models.Model):
    descripcion = models.CharField(max_length=200)
    non_neto = models.PositiveIntegerField('Contenido Neto')
    uni_med = models.CharField('Unidad de Medida',choices=UM_CHOICES, max_length=3)


    def __str__(self):
        return self.descripcion