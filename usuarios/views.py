from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import PerfilUsuario
from .forms import CrearUsuarioForm, PerfilUsuarioForm, EditarUsuarioForm
from .decorators import requiere_perfil


@login_required
@requiere_perfil('SUPER', 'DIRECTOR')
def lista_usuarios(request):
    usuarios = User.objects.select_related('perfil').order_by('last_name', 'first_name')
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})


@login_required
@requiere_perfil('SUPER', 'DIRECTOR')
def crear_usuario(request):
    user_form = CrearUsuarioForm(request.POST or None)
    perfil_form = PerfilUsuarioForm(request.POST or None)
    if user_form.is_valid() and perfil_form.is_valid():
        user = user_form.save()
        perfil = perfil_form.save(commit=False)
        perfil.user = user
        perfil.save()
        messages.success(request, f'Usuario {user.username} creado correctamente.')
        return redirect('lista_usuarios')
    return render(request, 'usuarios/form.html', {
        'user_form': user_form,
        'perfil_form': perfil_form,
        'titulo': 'Nuevo Usuario',
    })


@login_required
@requiere_perfil('SUPER', 'DIRECTOR')
def editar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    perfil, _ = PerfilUsuario.objects.get_or_create(user=usuario, defaults={'rol': 'SECRETARIA'})
    user_form = EditarUsuarioForm(request.POST or None, instance=usuario)
    perfil_form = PerfilUsuarioForm(request.POST or None, instance=perfil)
    if user_form.is_valid() and perfil_form.is_valid():
        user_form.save()
        perfil_form.save()
        messages.success(request, 'Usuario actualizado correctamente.')
        return redirect('lista_usuarios')
    return render(request, 'usuarios/form.html', {
        'user_form': user_form,
        'perfil_form': perfil_form,
        'titulo': 'Editar Usuario',
        'usuario': usuario,
    })


@login_required
@requiere_perfil('SUPER', 'DIRECTOR')
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if usuario == request.user:
        messages.error(request, 'No puedes eliminar tu propio usuario.')
        return redirect('lista_usuarios')
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado.')
        return redirect('lista_usuarios')
    return render(request, 'usuarios/confirmar_eliminar.html', {'usuario': usuario})


@login_required
def cambiar_password(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    # Solo directores/super pueden cambiar contraseña de otros; cualquiera puede cambiar la suya
    try:
        mi_perfil = request.user.perfil
        es_director = mi_perfil.es_director()
    except Exception:
        es_director = request.user.is_superuser
    if usuario != request.user and not es_director and not request.user.is_superuser:
        messages.error(request, 'No tienes permiso para cambiar esta contraseña.')
        return redirect('lista_usuarios')
    if request.method == 'POST':
        p1 = request.POST.get('password1', '')
        p2 = request.POST.get('password2', '')
        if not p1:
            messages.error(request, 'La contraseña no puede estar vacía.')
        elif p1 != p2:
            messages.error(request, 'Las contraseñas no coinciden.')
        elif len(p1) < 8:
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres.')
        else:
            usuario.set_password(p1)
            usuario.save()
            messages.success(request, f'Contraseña de {usuario.username} actualizada correctamente.')
            return redirect('lista_usuarios')
    return render(request, 'usuarios/cambiar_password.html', {'usuario': usuario})