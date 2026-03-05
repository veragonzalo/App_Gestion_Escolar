from django.shortcuts import render
from . import forms
from django.contrib.auth.decorators import login_required

@login_required
def portal_cursos(request):
    return render(request, 'cursos/inicio_cursos.html')


def lista_cursos(request):
    cursos = ["Kinder A", "Primer Basico C", "Segundo Basico A", "Terceiro Basico A", "Quarto Basico A", "Quinto Basico A"]
    contexto = {
        "lista_cursos": cursos
    }
    return render(request, 'cursos/lista_cursos.html', contexto)


def nuevo_curso(request):
    if request.method == "GET":
        form = forms.CursoForm()
    else:
        form = forms.CursoForm(request.POST)
        if form.is_valid():
            nombre_curso = form.cleaned_data['nombre_curso']
            contexto_post = {
                "nombre_curso": nombre_curso,
            }

            # aca se deberian tomar las variables y guardarlas en la base de datos
            # enviar mensaje de confirmacion " nuevo alumno ingresado exitosamente"
            return render(request, 'cursos/registro_exito.html', contexto_post)
    contexto = {
        "form": form
    }
    return render(request,'cursos/registro_curso.html', contexto)

