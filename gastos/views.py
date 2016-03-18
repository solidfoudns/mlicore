from django.shortcuts import render
from .forms import TipoGastoForm
# Create your views here.

def misGastos(request):
    return render(request, 'gastos.html')

def tipoGasto(request):
    form = TipoGastoForm()
    return render(request, 'tipo_gasto.html',{'form':form} )


def misInsumos(request):
    return render(request)


def tipoInsumo(request):
    return render(request)