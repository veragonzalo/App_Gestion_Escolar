from django import forms
from .models import Comunicado

INPUT_CLASS = 'w-full px-4 py-3 rounded-lg border border-slate-300 bg-white focus:outline-none focus:ring-2 focus:ring-[#002147] focus:border-transparent text-slate-800'


class ComunicadoForm(forms.ModelForm):
    class Meta:
        model = Comunicado
        fields = ['titulo', 'tipo', 'destinatarios', 'curso', 'contenido', 'activo']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Ej: Reunión de apoderados 1°A'
            }),
            'tipo': forms.Select(attrs={'class': INPUT_CLASS}),
            'destinatarios': forms.Select(attrs={'class': INPUT_CLASS}),
            'curso': forms.Select(attrs={'class': INPUT_CLASS}),
            'contenido': forms.Textarea(attrs={
                'class': INPUT_CLASS,
                'rows': 8,
                'placeholder': 'Redacta el comunicado aquí...'
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 text-[#002147] rounded border-slate-300 focus:ring-[#002147]'
            }),
        }