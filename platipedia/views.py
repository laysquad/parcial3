from django.shortcuts import render
from platipedia.models import Platillo, Ingrediente

# Create your views here.
def Principal(request):
    ListaPlatillos = Platillo.objects.all()
    ListaIngredientes = Ingrediente.objects.all()
    return render(request, 'platipedia/principal.html', {'ListaPlatillos':ListaPlatillos,'ListaIngredientes':ListaIngredientes})

def PlatilloDetalle(request,pk):
    vPlatillo = Platillo.objects.filter(id=pk)[0]
    vIngredientes = vPlatillo.ingredientes.all()
    return render(request, 'platipedia/PlatilloDetalle.html', {'Platillo':vPlatillo, 'Ingredientes':vIngredientes})

def IngredienteDetalle(request,pk):
    vIngrediente = Ingrediente.objects.filter(id=pk)[0]
    return render(request, 'platipedia/IngredienteDetalle.html', {'Ingrediente':vIngrediente})