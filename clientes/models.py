from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.TextField()
    telefono = models.PositiveIntegerField()
    correo = models.EmailField()

    def __str__(self):
        return self.nombre