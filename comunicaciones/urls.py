from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_comunicaciones, name='inicio_comunicaciones'),
    path('lista/', views.lista_comunicados, name='lista_comunicados'),
    path('crear/', views.crear_comunicado, name='crear_comunicado'),
    path('<int:pk>/', views.detalle_comunicado, name='detalle_comunicado'),
    path('<int:pk>/editar/', views.editar_comunicado, name='editar_comunicado'),
    path('<int:pk>/eliminar/', views.eliminar_comunicado, name='eliminar_comunicado'),
]