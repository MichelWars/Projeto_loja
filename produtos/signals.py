from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from produtos.models import Produto, ProdutoInventory


# def produto_inventory_update():
#     produto_count = Produto.objects.all().count()
#     produto_value = Produto.objects.aggregate(
#         total_value=Sum('value')
#     )['total_value']
#     ProdutoInventory.objects.create(
#         produto_count=produto_count,
#         produto_value=produto_value
#     )


# @receiver(post_save, sender=Produto)
# def produto_post_save(sender, instance, **kwargs):
#     produto_inventory_update()


# @receiver(post_delete, sender=Produto)
# def produto_post_delete(sender, instance, **kwargs):
#     produto_inventory_update()

# Essa signal coloca uma foto generica caso o usuario tente salvar o produto sem foto
@receiver(pre_save, sender=Produto)
def produto_pre_save(sender, instance, **kwargs):

    if not instance.foto:
        instance.foto = "produtos/sem_imagem.png"
