from django.urls import path
from . import views

urlpatterns = [
    path('', views.Principal, name='Principal'),
    path('platillodetalle/<int:pk>/', views.PlatilloDetalle, name='PlatilloDetalle'),
    path('ingredientedetalle/<int:pk>/', views.IngredienteDetalle, name='IngredienteDetalle'),
]