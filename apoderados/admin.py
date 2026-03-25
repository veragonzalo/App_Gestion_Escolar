from django.contrib import admin
from .models import Apoderado

@admin.register(Apoderado)
class ApoderadoAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellido', 'telefono', 'email']
    search_fields = ['rut', 'nombre', 'apellido', 'email']
