from django.urls import path
from . import views

urlpatterns = [
    # Portal
    path('', views.inicio_horarios, name='inicio_horarios'),

    # Asignaturas
    path('asignaturas/', views.lista_asignaturas, name='lista_asignaturas'),
    path('asignaturas/crear/', views.crear_asignatura, name='crear_asignatura'),
    path('asignaturas/<int:pk>/', views.detalle_asignatura, name='detalle_asignatura'),
    path('asignaturas/<int:pk>/editar/', views.editar_asignatura, name='editar_asignatura'),
    path('asignaturas/<int:pk>/eliminar/', views.eliminar_asignatura, name='eliminar_asignatura'),

    # Horarios (bloques)
    path('bloques/', views.lista_bloques, name='lista_bloques'),
    path('bloques/crear/', views.crear_bloque, name='crear_bloque'),
    path('bloques/<int:pk>/editar/', views.editar_bloque, name='editar_bloque'),
    path('bloques/<int:pk>/eliminar/', views.eliminar_bloque, name='eliminar_bloque'),

    # Vista horario semanal por curso
    path('curso/<int:curso_pk>/', views.horario_curso, name='horario_curso'),
]