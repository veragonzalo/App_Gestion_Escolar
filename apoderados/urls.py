from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.portal_apoderados, name='inicio_apoderados'),
    path('lista/', views.lista_apoderados, name='lista_apoderados'),
    path('registrar/', views.nuevo_apoderado, name='registrar_apoderado'),
    path('detalle/<str:apoderado_rut>/', views.detalle_apoderado, name='detalle_apoderado'),
    path('editar/<str:apoderado_rut>/', views.editar_apoderado, name='editar_apoderado'),
    path('eliminar/<str:apoderado_rut>/', views.eliminar_apoderado, name='eliminar_apoderado'),
]
