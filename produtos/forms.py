from django import forms
from produtos.models import Produto


# formulario de cadastro de produtos
class ProdModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

# validação de valor
    # def clean_value(self):
    #     value = self.cleaned_data.get('value')
    #     if value < 20000:
    #         self.add_error('value', 'Valor mínimo do carro deve ser de R$20.000')
    #     return value

# validação de ano
    # def clean_factory_year(self):
    #     factory_year = self.cleaned_data.get('factory_year')
    #     if factory_year < 1975:
    #         self.add_error('factory_year', 'Não é possível cadastrar carros fabricados antes de 1975')
    #     return factory_year
