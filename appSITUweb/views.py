from django.shortcuts import render
from .forms import PasajeroFormulario
from .models import Pasajero
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def home_view(request):
    return render(request, "index.html", {})


def pasajeros(request):
    data = PasajeroFormulario()    
    pasajeros = Pasajero.objects.all()
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()

    return render(request, "pasajeros.html", {"pasajeros": pasajeros, 'form': data})


def pasajeros_create(request):
    pasajero = Pasajero()
    data = {
        'form': PasajeroFormulario(instance=pasajero)
    }
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, instance=pasajero, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="pasajeros")

    return render(request, 'pasajerosEdit.html', data)


def pasajeros_edit(request, id):
    """
    Funciona para editar
    """
    pasajero = get_object_or_404(Pasajero, id=id)
    data = {
        'form': PasajeroFormulario(instance=pasajero)
    }
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, instance=pasajero, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="pasajeros")

    return render(request, 'pasajerosEdit.html', data)


def pasajeros_delete(request, id):
    """
    Funciona para eliminar
    """
    pasajero = get_object_or_404(Pasajero, id=id)

    if pasajero:
        pasajero.delete()

    return redirect(to="pasajeros")

