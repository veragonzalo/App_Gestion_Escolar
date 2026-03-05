from django.shortcuts import render
from . import forms
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def portal_profesores(request):
    return render (request, 'profesores/inicio_profesores.html')

def lista_profesores(request):
    profesores = ["Juan Mayorga", "Omar Monsalve", "Felix Cañoles", "Sergio Perez", "Leticia  Ojeda"]
    contexto = {
        "lista_profesores": profesores
    }
    return render(request, 'profesores/lista_profesores.html', contexto)

def nuevo_profesor(request):
    if request.method == "GET":
        form = forms.ProfesorForm()
    else:
        form = forms.ProfesorForm(request.POST)
        if form.is_valid():
            nombre_profesor = form.cleaned_data['nombre_profesor']
            apellido_profesor = form.cleaned_data['apellido_profesor']
            edad_profesor = form.cleaned_data['edad_profesor']
            curso_profesor = form.cleaned_data['curso_profesor']
            contexto_post = {
                "nombre_profesor": nombre_profesor,
                "apellido_profesor": apellido_profesor,
                "edad_profesor": edad_profesor,
                "curso_profesor": curso_profesor
            }

            # aca se deberian tomar las variables y guardarlas en la base de datos
            # enviar mensaje de confirmacion " nuevo alumno ingresado exitosamente"
            return render(request, 'profesores/registro_exito.html', contexto_post)
    contexto = {
        "form": form
    }
    return render(request,'profesores/registro_profesores.html', contexto)
# Create your views here.
