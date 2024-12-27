from django import forms
from .models import Laboratorio

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['nombre', 'ciudad', 'pais']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ingrese el nombre del laboratorio',
                'class': 'form-control',
            }),
            'ciudad': forms.TextInput(attrs={
                'placeholder': 'Ingrese la ciudad',
                'class': 'form-control',
            }),
            'pais': forms.TextInput(attrs={
                'placeholder': 'Ingrese el país',
                'class': 'form-control',
            }),
        }

