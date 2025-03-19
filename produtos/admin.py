from django.contrib import admin
from produtos.models import Produto




class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'console', 'ano_lancamento', 'valor', 'foto', 'descricao')
    search_fields = ('titulo', 'console', 'ano_lancamento', 'valor', 'descricao')



admin.site.register(Produto, ProdutoAdmin)
