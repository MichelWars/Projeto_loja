from django import forms

from .models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['forma_pagamento', 'parcelas', 'endereco']
        widgets = {
            'forma_pagamento': forms.Select(attrs={'class': 'form-control'}),
            'parcelas': forms.Select(attrs={'class': 'form-control'}),
            'endereco': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 2}
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        forma_pagamento = cleaned_data.get('forma_pagamento')
        parcelas = cleaned_data.get('parcelas')

        if forma_pagamento == 'credito' and not parcelas:
            self.add_error(
                'parcelas',
                'Informe a quantidade de parcelas para pagamento com cartão de crédito.',
            )
        elif forma_pagamento != 'credito':
            cleaned_data['parcelas'] = None

        return cleaned_data
