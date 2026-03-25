from django import forms
from datetime import date
from .models import Nota

TAILWIND_INPUT = 'w-full px-4 py-3 rounded-lg border border-slate-300 bg-white text-slate-900 focus:ring-2 focus:ring-[#002147] focus:border-[#002147] outline-none transition-all'


class NotaForm(forms.ModelForm):

    fecha = forms.DateField(
        label='Fecha',
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': TAILWIND_INPUT,
        }),
        input_formats=['%Y-%m-%d', '%d-%m-%Y', '%d/%m/%Y'],
    )

    class Meta:
        model = Nota
        fields = ['alumno', 'curso', 'tipo_evaluacion', 'nota', 'fecha', 'descripcion']
        widgets = {
            'alumno': forms.Select(attrs={'class': TAILWIND_INPUT}),
            'curso': forms.Select(attrs={'class': TAILWIND_INPUT}),
            'tipo_evaluacion': forms.Select(attrs={'class': TAILWIND_INPUT}),
            'nota': forms.NumberInput(attrs={
                'class': TAILWIND_INPUT,
                'step': '0.1',
                'min': '1.0',
                'max': '7.0',
                'placeholder': 'Ej: 5.5',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': TAILWIND_INPUT + ' resize-none',
                'rows': 3,
                'placeholder': 'Descripción opcional de la evaluación...',
            }),
        }

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha and fecha > date.today():
            raise forms.ValidationError('La fecha no puede ser futura.')
        return fecha

    def clean_nota(self):
        nota = self.cleaned_data.get('nota')
        if nota is not None:
            if nota < 1.0 or nota > 7.0:
                raise forms.ValidationError('La nota debe estar entre 1.0 y 7.0.')
        return nota
