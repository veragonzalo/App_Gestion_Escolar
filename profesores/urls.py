from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.portal_profesores, name="inicio_profesores"),
    path("lista_profesores/", views.lista_profesores, name="lista_profesores"),
    path("registrar_profesor/", views.nuevo_profesor, name="registrar_profesor"),

    path('detalle/<str:rut>/', views.detalle_profesor, name='detalle_profesor'),

    path('editar/<str:rut>/', views.editar_profesor, name='editar_profesor'),

    path('eliminar/<str:rut>/', views.eliminar_profesor, name='eliminar_profesor'),
]



