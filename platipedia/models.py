from django.db import models
from django.utils import timezone
from django.contrib import admin

class Usuario(models.Model):
    usuario = models.CharField(max_length=16)
    contraseña = models.CharField(max_length=16)
    nombre = models.CharField(max_length=100)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    contenido = models.TextField()
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    creado = models.DateTimeField(
            default=timezone.now)
    publicado = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.publicado = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre

class Platillo(models.Model):
    nombre = models.CharField(max_length=50)
    contenido = models.TextField()
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    creado = models.DateTimeField(
            default=timezone.now)
    publicado = models.DateTimeField(
            blank=True, null=True)
    ingredientes = models.ManyToManyField(Ingrediente,through='Relacion')

    def publish(self):
        self.publicado = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre

class Relacion (models.Model):
    platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)

class RelacionInLine(admin.TabularInline):
    model = Relacion
    extra = 1

class PlatilloAdmin(admin.ModelAdmin):
    inlines = (RelacionInLine,)

class IngredienteAdmin (admin.ModelAdmin):
    inlines = (RelacionInLine,)