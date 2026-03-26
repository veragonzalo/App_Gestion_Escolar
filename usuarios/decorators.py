from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages


def requiere_perfil(*roles):
    """
    Restringe el acceso a usuarios cuyo rol esté en la lista.
    Uso: @requiere_perfil('SUPER', 'DIRECTOR')
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            try:
                perfil = request.user.perfil
                if perfil.rol in roles:
                    return view_func(request, *args, **kwargs)
            except Exception:
                pass
            messages.error(request, 'No tienes permisos para acceder a esta sección.')
            return redirect('inicio')
        return wrapper
    return decorator


def requiere_puede_editar(view_func):
    """Solo Director, Secretaria y Super pueden crear/editar/eliminar registros administrativos."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        try:
            if request.user.perfil.puede_editar():
                return view_func(request, *args, **kwargs)
        except Exception:
            pass
        messages.error(request, 'No tienes permisos para realizar esta acción.')
        return redirect('inicio')
    return wrapper


def requiere_academico(view_func):
    """Solo Director, Profesor y Super pueden editar notas y asistencia."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        try:
            if request.user.perfil.puede_editar_academico():
                return view_func(request, *args, **kwargs)
        except Exception:
            pass
        messages.error(request, 'No tienes permisos para realizar esta acción.')
        return redirect('inicio')
    return wrapper