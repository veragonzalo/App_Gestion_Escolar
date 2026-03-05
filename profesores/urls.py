from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.portal_profesores, name="inicio_profesores"),
    path("lista_profesores/", views.lista_profesores, name="lista_profesores"),
    path("registrar_profesor/", views.nuevo_profesor, name="registrar_profesor"),
]



