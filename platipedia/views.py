from django.shortcuts import render

# Create your views here.
def Principal(request):
    return render(request, 'platipedia/base.html', {})