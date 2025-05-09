from django import forms
from produtos.models import Produto


# formulario de cadastro de produtos
class ProdModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['titulo', 'console', 'ano_lancamento', 'valor', 'foto', 'descricao']
        # widgets = {
        #     'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        #     'console': forms.Select(attrs={'class': 'form-control'}),
        #     'brand': forms.Select(attrs={'class': 'form-control'}),
        #     'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows':1}),
        #     'serie_number': forms.TextInput(attrs={'class': 'form-control'}),
        #     'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
        # }
        # labels = {
        #     'titulo': 'Titulo',
        #     'console': 'Categoria',
        #     'brand': 'Marca',
        #     'descricao': 'Descrição',
        #     'serie_number': 'Numero de Serie',
        #     'cost_price': 'Preço de Custo',
        #     'selling_price': 'Preço de Venda',
        # }
