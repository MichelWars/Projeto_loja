from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ItemPedido


# sempre que um pedido é gerado, reduz a quantidade de itens no estoque referente e quantidade vendida no pedido
@receiver(post_save, sender=ItemPedido)
def update_produto_quantidade(sender, instance, created, **kwargs):
    if created:   # somente se for gerado um NOVO registro em Outflow
        if (
            instance.quantidade > 0
        ):   # verifica se a quantidade de saida é maior que zero
            produto = (
                instance.produto
            )   # verifica o produto na instancia de saida
            produto.quantidade -= (
                instance.quantidade
            )   # altera a quantidade em product
            produto.save()
