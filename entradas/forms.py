from django import forms
from . import models

class EntradaForm(forms.ModelForm):

    class Meta:
        model = models.Entrada
        fields = ['produto', 'quantidade']
        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),

        }   
        labels = {
            'produto': 'Produto',
            'quantidade': 'Quantidade',

        }