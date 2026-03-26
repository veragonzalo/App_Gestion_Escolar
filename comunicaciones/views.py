from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Comunicado
from .forms import ComunicadoForm


@login_required
def inicio_comunicaciones(request):
    recientes = Comunicado.objects.filter(activo=True)[:6]
    contexto = {
        'total': Comunicado.objects.count(),
        'total_activos': Comunicado.objects.filter(activo=True).count(),
        'urgentes': Comunicado.objects.filter(tipo='UR', activo=True).count(),
        'recientes': recientes,
    }
    return render(request, 'comunicaciones/inicio.html', contexto)


@login_required
def lista_comunicados(request):
    tipo = request.GET.get('tipo')
    comunicados = Comunicado.objects.select_related('autor', 'curso')
    if tipo:
        comunicados = comunicados.filter(tipo=tipo)
    return render(request, 'comunicaciones/lista.html', {
        'comunicados': comunicados,
        'tipo_filtro': tipo,
    })


@login_required
def crear_comunicado(request):
    form = ComunicadoForm(request.POST or None)
    if form.is_valid():
        comunicado = form.save(commit=False)
        comunicado.autor = request.user
        comunicado.save()
        return redirect('detalle_comunicado', pk=comunicado.pk)
    return render(request, 'comunicaciones/form.html', {'form': form, 'titulo': 'Nuevo Comunicado'})


@login_required
def detalle_comunicado(request, pk):
    comunicado = get_object_or_404(Comunicado, pk=pk)
    return render(request, 'comunicaciones/detalle.html', {'comunicado': comunicado})


@login_required
def editar_comunicado(request, pk):
    comunicado = get_object_or_404(Comunicado, pk=pk)
    form = ComunicadoForm(request.POST or None, instance=comunicado)
    if form.is_valid():
        form.save()
        return redirect('detalle_comunicado', pk=pk)
    return render(request, 'comunicaciones/form.html', {'form': form, 'titulo': 'Editar Comunicado', 'comunicado': comunicado})


@login_required
def eliminar_comunicado(request, pk):
    comunicado = get_object_or_404(Comunicado, pk=pk)
    if request.method == 'POST':
        comunicado.delete()
        return redirect('lista_comunicados')
    return render(request, 'comunicaciones/confirmar_eliminar.html', {'comunicado': comunicado})