from django.contrib import admin
from .models import Profesor


class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'fecha_nacimiento', 'profesion')
    search_fields = ('rut', 'nombre', 'apellido')
    list_filter = ('profesion',)
    ordering = ('apellido', 'nombre')


admin.site.register(Profesor, ProfesorAdmin)
