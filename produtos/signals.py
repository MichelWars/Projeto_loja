from django.db.models import F, Sum
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver

from gemini_api.client import get_descricao_produto
from produtos.models import Produto, ProdutoInventario


# Essa signal atualiza o estoque sempre que um produto for adicionado ou removido
def produto_inventario_update():
    # Soma total de todas as quantidades
    contador_produtos = (
        Produto.objects.aggregate(total_itens=Sum('quantidade'))['total_itens']
        or 0
    )

    # Soma valor_estoque = quantidade * valor unitário para cada produto
    valor_estoque = (
        Produto.objects.aggregate(
            total_valor=Sum(F('quantidade') * F('valor'))
        )['total_valor']
        or 0
    )

    ProdutoInventario.objects.create(
        contador_produtos=contador_produtos, valor_estoque=valor_estoque
    )


# Essa signal atualiza o estoque sempre que um produto for adicionado ou removido
@receiver(post_save, sender=Produto)
def produto_post_save(sender, instance, **kwargs):
    produto_inventario_update()


# Essa signal atualiza o estoque sempre que um produto for adicionado ou removido
@receiver(post_delete, sender=Produto)
def produto_post_delete(sender, instance, **kwargs):
    produto_inventario_update()


# Essa signal coloca uma foto generica caso o usuario tente salvar o produto sem foto
@receiver(pre_save, sender=Produto)
def produto_pre_save(sender, instance, **kwargs):

    if not instance.foto:
        instance.foto = 'produtos/sem_imagem.png'

    # cadastra um descricao automatica para o produto usando Gemini IA
    if not instance.descricao:
        ai_bio = get_descricao_produto(
            instance.titulo, instance.console, instance.ano_lancamento
        )
        instance.descricao = ai_bio
