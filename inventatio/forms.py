from django import forms
from .models import Articulo, Categoria, Provedor

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['nombre', 'descripcion', 'categoria', 'provedor', 'precio_costo', 'precio_venta', 'cantidad']

class CategoriasForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion']

class ProvedorForm(forms.ModelForm):
    class Meta:
        model = Provedor
        fields = ['descripcion']