from django import forms


class CursoForm(forms.Form):
    nombre_curso = forms.CharField(
        label='Nombre del Curso',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ej: Matemáticas 3° Medio A'
        })
    )

    def clean_nombre_curso(self):
        nombre = self.cleaned_data.get('nombre_curso')
        if nombre:
            nombre = nombre.strip()
            if len(nombre) < 3:
                raise forms.ValidationError('El nombre del curso debe tener al menos 3 caracteres.')
        return nombre