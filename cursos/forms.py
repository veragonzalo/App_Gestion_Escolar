from django import forms

class CursoForm(forms.Form):
    nombre_curso = forms.CharField(label='Nombre Curso', max_length=100)


