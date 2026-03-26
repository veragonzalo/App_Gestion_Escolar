from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.portal_notas, name='inicio_notas'),
    path('lista/', views.lista_notas, name='lista_notas'),
    path('registrar/', views.registrar_nota, name='registrar_nota'),
    path('detalle/<int:nota_id>/', views.detalle_nota, name='detalle_nota'),
    path('editar/<int:nota_id>/', views.editar_nota, name='editar_nota'),
    path('eliminar/<int:nota_id>/', views.eliminar_nota, name='eliminar_nota'),
    path('boletin/', views.boletin_notas, name='boletin_notas'),
    path('boletin/exportar/', views.exportar_boletin_csv, name='exportar_boletin_csv'),
]
