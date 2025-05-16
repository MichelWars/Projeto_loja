from django import forms

from produtos.models import Produto


# formulario de cadastro de produtos
class ProdModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'titulo',
            'console',
            'ano_lancamento',
            'valor',
            'foto',
            'descricao',
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'console': forms.Select(attrs={'class': 'form-control'}),
            'ano_lancamento': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
        }
