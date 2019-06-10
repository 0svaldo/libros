from django.contrib import admin

# Register your models here.

from .models import Generos, Autores, Ubicacion, Libros

admin.site.register(Generos)
admin.site.register(Autores)
admin.site.register(Ubicacion)
admin.site.register(Libros)