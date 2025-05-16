from django.contrib import admin

from produtos.models import Produto, ProdutoInventario


# visualização da tabela Produtos no admin do django
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'console',
        'ano_lancamento',
        'valor',
        'foto',
        'descricao',
    )
    search_fields = (
        'titulo',
        'console',
        'ano_lancamento',
        'valor',
        'descricao',
    )


class ProdutoInventarioAdmin(admin.ModelAdmin):
    list_display = ('contador_produtos', 'valor_estoque', 'data_atualizacao')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(ProdutoInventario, ProdutoInventarioAdmin)
