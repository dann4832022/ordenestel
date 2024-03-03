from django import forms
from .models import ArchivoExcel

class ArchivoExcelForm(forms.ModelForm):
    class Meta:
        model = ArchivoExcel
        fields = ['nombre', 'archivo']

