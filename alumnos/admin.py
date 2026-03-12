from django.contrib import admin
from .models import Alumno


class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'fecha_nacimiento')
    search_fields = ('rut', 'nombre', 'apellido')
    ordering = ('apellido', 'nombre')


admin.site.register(Alumno, AlumnoAdmin)
