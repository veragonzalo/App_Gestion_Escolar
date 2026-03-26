from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.portal_alumnos, name="inicio_alumnos"),
    path('lista_alumnos/', views.lista_alumnos, name="lista_alumnos"),
    path('registrar_alumno/', views.nuevo_alumno, name="registrar_alumno"),

    # NUEVAS RUTAS
    path('detalle/<str:alumno_rut>/', views.detalle_alumno, name='detalle_alumno'),

    path('editar/<str:alumno_rut>/', views.editar_alumno, name='editar_alumno'),

    path('eliminar/<str:alumno_rut>/', views.eliminar_alumno, name='eliminar_alumno'),
    path('perfil/<str:alumno_rut>/', views.perfil_alumno, name='perfil_alumno'),
]

