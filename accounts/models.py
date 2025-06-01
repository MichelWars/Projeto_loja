from django.contrib.auth.models import User
from django.db import models


# cliente são criados baseado na model User do django
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
