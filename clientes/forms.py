__author__ = 'mrk2'
from  django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'direccion', 'telefono', 'correo')