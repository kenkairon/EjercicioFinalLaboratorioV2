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
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        qs = Laboratorio.objects.filter(nombre=nombre)

        # Excluir la instancia actual en caso de edición
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError("Este laboratorio ya existe en la base de datos.")

        return nombre