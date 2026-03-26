from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.portal_asistencia, name='inicio_asistencia'),
    path('lista/', views.lista_asistencia, name='lista_asistencia'),
    path('registrar/', views.registrar_asistencia, name='registrar_asistencia'),
    path('detalle/<int:asistencia_id>/', views.detalle_asistencia, name='detalle_asistencia'),
    path('editar/<int:asistencia_id>/', views.editar_asistencia, name='editar_asistencia'),
    path('eliminar/<int:asistencia_id>/', views.eliminar_asistencia, name='eliminar_asistencia'),
    path('resumen/', views.resumen_asistencia, name='resumen_asistencia'),
]
