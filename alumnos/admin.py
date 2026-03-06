from django.contrib import admin
from . models import Alumno

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'edad', 'curso')
    search_fields = ('nombre', 'apellido')


admin.site.register(Alumno, AlumnoAdmin)

