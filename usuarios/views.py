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