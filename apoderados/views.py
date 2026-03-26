from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Apoderado
from .forms import ApoderadoForm
from usuarios.decorators import requiere_puede_editar


@login_required
def portal_apoderados(request):
    total_apoderados = Apoderado.objects.count()
    con_alumnos = Apoderado.objects.filter(alumnos__isnull=False).distinct().count()
    contexto = {
        'total_apoderados': total_apoderados,
        'con_alumnos': con_alumnos,
        'sin_alumnos': total_apoderados - con_alumnos,
    }
    return render(request, 'apoderados/inicio.html', contexto)


@login_required
def lista_apoderados(request):
    apoderados = Apoderado.objects.prefetch_related('alumnos').all()
    return render(request, 'apoderados/lista_apoderados.html', {'lista_apoderados': apoderados})


@login_required
def detalle_apoderado(request, apoderado_rut):
    apoderado = get_object_or_404(Apoderado, rut=apoderado_rut)
    return render(request, 'apoderados/detalle_apoderado.html', {'apoderado': apoderado})


@login_required
@requiere_puede_editar
def nuevo_apoderado(request):
    if request.method == 'POST':
        form = ApoderadoForm(request.POST)
        if form.is_valid():
            apoderado = form.save()
            messages.success(request, f'Apoderado {apoderado.nombre} {apoderado.apellido} registrado exitosamente.')
            return redirect('lista_apoderados')
        else:
            messages.error(request, 'Por favor corrija los errores del formulario.')
    else:
        form = ApoderadoForm()
    return render(request, 'apoderados/registro_apoderado.html', {'form': form})


@login_required
@requiere_puede_editar
def editar_apoderado(request, apoderado_rut):
    apoderado = get_object_or_404(Apoderado, rut=apoderado_rut)
    if request.method == 'POST':
        form = ApoderadoForm(request.POST, instance=apoderado)
        if form.is_valid():
            form.save()
            messages.success(request, f'Apoderado {apoderado.nombre} {apoderado.apellido} actualizado exitosamente.')
            return redirect('lista_apoderados')
    else:
        form = ApoderadoForm(instance=apoderado)
    return render(request, 'apoderados/editar_apoderado.html', {'form': form, 'apoderado': apoderado})


@login_required
@requiere_puede_editar
def eliminar_apoderado(request, apoderado_rut):
    apoderado = get_object_or_404(Apoderado, rut=apoderado_rut)
    if request.method == 'POST':
        nombre_completo = f"{apoderado.nombre} {apoderado.apellido}"
        apoderado.delete()
        messages.success(request, f'Apoderado {nombre_completo} eliminado exitosamente.')
        return redirect('lista_apoderados')
    return render(request, 'apoderados/confirmar_eliminar.html', {'apoderado': apoderado})