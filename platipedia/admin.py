from django.contrib import admin
from platipedia.models import Usuario, Platillo, PlatilloAdmin, Ingrediente, IngredienteAdmin

admin.site.register(Platillo, PlatilloAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)

# Register your models here.
