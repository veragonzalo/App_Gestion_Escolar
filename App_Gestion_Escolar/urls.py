"""
URL configuration for App_Gestion_Escolar project.
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Página principal
    path('', views.inicio, name="inicio"),

    # Apps
    path("alumnos/", include("alumnos.urls")),
    path("cursos/", include("cursos.urls")),
    path("profesores/", include("profesores.urls")),
    path("asistencia/", include("asistencia.urls")),
    path("notas/", include("notas.urls")),
    path("apoderados/", include("apoderados.urls")),
    path("horarios/", include("horarios.urls")),
    path("comunicaciones/", include("comunicaciones.urls")),
    path("usuarios/", include("usuarios.urls")),

    # Autenticación
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # Logout desde las APPS (redirige directo a login)
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),

    # Logout desde el ADMIN (muestra página de confirmación)
    path('admin/logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='admin_logout'),
]

