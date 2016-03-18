from django.contrib import admin
from .models import Provedor, Categoria, Articulo
# Register your models here.

@admin.register(Provedor)
class ProvedorAdmin(admin.ModelAdmin):
    pass

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass
@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    pass