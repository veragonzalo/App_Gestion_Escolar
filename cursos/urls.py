from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.portal_cursos, name="inicio_cursos"),
    path("lista_cursos/", views.lista_cursos, name="lista_cursos"),
    path('registrar_curso/', views.nuevo_curso, name="registrar_curso"),

    path('<int:codigo>/', views.detalle_curso, name='detalle_curso'),

    path('<int:codigo>/editar/', views.editar_curso, name='editar_curso'),

    path('<int:codigo>/eliminar/', views.eliminar_curso, name='eliminar_curso'),
]
