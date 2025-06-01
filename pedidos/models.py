from django.contrib.auth.models import User
from django.db import models

from produtos.models import Produto


# Essa classe representa um pedido no banco de dados
class Pedido(models.Model):
    FORMA_PAGAMENTO_CHOICES = [
        ('pix', 'PIX'),
        ('boleto', 'Boleto Bancário'),
        ('credito', 'Cartão de Crédito'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    forma_pagamento = models.CharField(
        max_length=20, choices=FORMA_PAGAMENTO_CHOICES
    )
    parcelas = models.PositiveIntegerField(blank=True, null=True)
    endereco = models.TextField()

    def __str__(self):
        return f'Pedido #{self.id} de {self.usuario.username}'

    # soma o subtotal de todos os itens do pedido
    def get_total(self):
        return sum(item.subtotal() for item in self.itens.all())


# Essa classe representa um item de pedido no banco de dados
class ItemPedido(models.Model):
    pedido = models.ForeignKey(
        Pedido, on_delete=models.CASCADE, related_name='itens'
    )
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    # soma o subtotal de todos os itens do pedido
    def subtotal(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f'{self.quantidade}x {self.produto.titulo}'
