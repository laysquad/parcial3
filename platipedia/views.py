from django.shortcuts import render
from platipedia.models import Platillo, Ingrediente

# Create your views here.
def Principal(request):
    ListaPlatillos = Platillo.objects.all()
    ListaIngredientes = Ingrediente.objects.all()
    return render(request, 'platipedia/base.html', {'ListaPlatillos':ListaPlatillos,'ListaIngredientes':ListaIngredientes})