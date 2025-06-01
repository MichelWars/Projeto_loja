from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Entrada


# sempre que uma entrada é gerada, aumenta a quantidade de itens no estoque
@receiver(post_save, sender=Entrada)
def update_produto_quantidade(sender, instance, created, **kwargs):
    if created:   # somente se for gerado um NOVO registro em Entrada
        if (
            instance.quantidade > 0
        ):   # verifica se a quantidade de entrada é maior que zero
            produto = (
                instance.produto
            )   # verifica o produto na instancia de entrada
            produto.quantidade += (
                instance.quantidade
            )   # altera a quantidade em produto
            produto.save()
