from django import forms
from .models import Curso
from profesores.models import Profesor
from alumnos.models import Alumno


class CursoForm(forms.ModelForm):
    """Formulario basado en el modelo Curso con estilos consistentes"""

    class Meta:
        model = Curso
        fields = ['nombre', 'profesor', 'alumnos']

        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: Matemáticas 3° Medio A',
                'class': 'w-full pl-12 pr-4 py-3 rounded-lg border border-slate-300 text-slate-900 focus:ring-2 focus:ring-amber-500 focus:border-amber-500 outline-none transition-all'
            }),

            'profesor': forms.Select(attrs={
                'class': 'w-full pl-12 pr-4 py-3 rounded-lg border border-slate-300 text-slate-900 focus:ring-2 focus:ring-amber-500 focus:border-amber-500 outline-none transition-all bg-white'
            }),

            'alumnos': forms.SelectMultiple(attrs={
                'class': 'w-full pl-12 pr-4 py-3 rounded-lg border border-slate-300 text-slate-900 focus:ring-2 focus:ring-amber-500 focus:border-amber-500 outline-none transition-all bg-white',
                'size': '8'
            }),
        }

        labels = {
            'nombre': 'Nombre del Curso',
            'profesor': 'Profesor Asignado',
            'alumnos': 'Alumnos Inscritos'
        }

        help_texts = {
            'profesor': 'Seleccione el profesor que impartirá este curso',
            'alumnos': 'Mantén Ctrl/Cmd para seleccionar múltiples alumnos'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Profesores ordenados
        self.fields['profesor'].queryset = Profesor.objects.all().order_by('apellido', 'nombre')
        self.fields['profesor'].empty_label = "-- Seleccione un profesor --"

        # Alumnos ordenados
        self.fields['alumnos'].queryset = Alumno.objects.all().order_by('apellido', 'nombre')

        # Campo alumnos opcional
        self.fields['alumnos'].required = False

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')

        if nombre:
            nombre = nombre.strip()

            if len(nombre) < 3:
                raise forms.ValidationError(
                    'El nombre del curso debe tener al menos 3 caracteres.'
                )

        return nombre