from django import forms
from django.contrib.auth.models import User
from .models import Cliente
from django.core.exceptions import ValidationError

# formulario de cadastro de clientes unindo campos da tabela User do django e da tabela Cliente
class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    password2 = forms.CharField(label="Confirme a senha", widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))

    nome = forms.CharField(max_length=100)
    sobrenome = forms.CharField(max_length=100)
    cpf = forms.CharField(max_length=11)
    telefone = forms.CharField(max_length=20)
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    # campos da tabela Cliente
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'nome', 'sobrenome', 'cpf', 'telefone', 'data_nascimento']

    # validação de senha
    def clean_password2(self):
        if self.cleaned_data.get("password1") != self.cleaned_data.get("password2"):
            raise ValidationError("As senhas não coincidem.")
        return self.cleaned_data.get("password2")

    # validação de e-mail
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(username=email).exists():
            raise ValidationError("Este e-mail já está em uso.")
        return email

    # cria o user e o cliente
    def save(self, commit=True):
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password1"]

        user = User.objects.create_user(username=email, email=email, password=password, first_name=self.cleaned_data["nome"], last_name=self.cleaned_data["sobrenome"])

        Cliente.objects.create(
            user=user,
            nome=self.cleaned_data["nome"],
            sobrenome=self.cleaned_data["sobrenome"],
            cpf=self.cleaned_data["cpf"],
            telefone=self.cleaned_data["telefone"],
            data_nascimento=self.cleaned_data["data_nascimento"]
        )

        return user
