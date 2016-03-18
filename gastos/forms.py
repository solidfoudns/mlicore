__author__ = 'seader'
from  .models import TipoGasto
from django import forms

class TipoGastoForm(forms.ModelForm):
    class Meta:
        model = TipoGasto
        fields = ('nombre',)