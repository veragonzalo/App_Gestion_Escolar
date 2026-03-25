from django import forms
from datetime import date
from .models import Asistencia

TAILWIND_INPUT = 'w-full px-4 py-3 rounded-lg border border-slate-300 bg-white text-slate-900 focus:ring-2 focus:ring-[#002147] focus:border-[#002147] outline-none transition-all'


class AsistenciaForm(forms.ModelForm):

    fecha = forms.DateField(
        label='Fecha',
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': TAILWIND_INPUT,
        }),
        input_formats=['%Y-%m-%d', '%d-%m-%Y', '%d/%m/%Y'],
    )

    class Meta:
        model = Asistencia
        fields = ['fecha', 'curso', 'alumno', 'estado', 'observacion']
        widgets = {
            'curso': forms.Select(attrs={'class': TAILWIND_INPUT}),
            'alumno': forms.Select(attrs={'class': TAILWIND_INPUT}),
            'estado': forms.Select(attrs={'class': TAILWIND_INPUT}),
            'observacion': forms.Textarea(attrs={
                'class': TAILWIND_INPUT + ' resize-none',
                'rows': 3,
                'placeholder': 'Observación opcional...',
            }),
        }

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha and fecha > date.today():
            raise forms.ValidationError('La fecha no puede ser futura.')
        return fecha
