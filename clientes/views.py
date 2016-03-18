from django.shortcuts import render
from .forms import ClienteForm
# Create your views here.


def clientes(request):
    return render(request, 'clientes.html')

def cliente(request):
    form = ClienteForm()
    return render(request, 'cliente.html', {
                                                "form":form
    })