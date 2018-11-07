from django.shortcuts import render
from platipedia.models import Platillo

# Create your views here.
def Principal(request):
    ListaPlatillos = Platillo.objects.all()
    return render(request, 'platipedia/base.html', {'ListaPlatillos':ListaPlatillos})