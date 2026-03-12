from django import forms
from .models import Curso
from profesores.models import Profesor
from alumnos.models import Alumno


class CursoForm(forms.ModelForm):
    """Formulario basado en el modelo Curso con selectores mejorados"""

    class Meta:
        model = Curso
        fields = ['nombre', 'profesor', 'alumnos']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: Matemáticas 3° Medio A',
                'class': 'form-control'
            }),
            'profesor': forms.Select(attrs={
                'class': 'form-control',
                'style': 'width: 100%; padding: 12px; border: 1px solid #cbd5e1; border-radius: 8px;'
            }),
            'alumnos': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'style': 'width: 100%; padding: 12px; border: 1px solid #cbd5e1; border-radius: 8px; min-height: 200px;',
                'size': '10'
            }),
        }
        labels = {
            'nombre': 'Nombre del Curso',
            'profesor': 'Profesor Asignado',
            'alumnos': 'Alumnos Inscritos (mantén Ctrl/Cmd para seleccionar múltiples)'
        }
        help_texts = {
            'profesor': 'Seleccione el profesor que impartirá este curso',
            'alumnos': 'Seleccione uno o más alumnos para inscribir en este curso (opcional)'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Personalizar el queryset y la representación del profesor
        self.fields['profesor'].queryset = Profesor.objects.all().order_by('apellido', 'nombre')
        self.fields['profesor'].empty_label = "-- Seleccione un profesor --"

        # Personalizar el queryset de alumnos
        self.fields['alumnos'].queryset = Alumno.objects.all().order_by('apellido', 'nombre')

        # Hacer que alumnos no sea requerido (se puede crear un curso sin alumnos)
        self.fields['alumnos'].required = False

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre:
            nombre = nombre.strip()
            if len(nombre) < 3:
                raise forms.ValidationError('El nombre del curso debe tener al menos 3 caracteres.')
        return nombre