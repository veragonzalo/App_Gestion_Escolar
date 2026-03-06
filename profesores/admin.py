from django.contrib import admin
from . models import Profesor

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'fecha_nacimiento', 'profesion')
    search_fields = ('rut', 'nombre')

admin.site.register(Profesor, ProfesorAdmin)


# Register your models here.
