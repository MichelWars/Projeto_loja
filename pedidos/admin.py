from django.contrib import admin

from .models import ItemPedido, Pedido


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    readonly_fields = ['produto', 'quantidade', 'preco_unitario', 'subtotal']
    can_delete = True  # já é o valor padrão, mas pode deixar explícito

    def subtotal(self, obj):
        return f'R$ {obj.subtotal():.2f}'

    subtotal.short_description = 'Subtotal'


class PedidoAdmin(admin.ModelAdmin):
    list_display = [
        'numero_pedido',
        'usuario',
        'total_pedido',
        'forma_pagamento',
        'parcelas_formatadas',
        'endereco_resumido',
        'criado_em',
        'listar_itens',
    ]
    list_filter = ['forma_pagamento', 'criado_em']
    search_fields = ['usuario__username', 'id']
    inlines = [ItemPedidoInline]
    readonly_fields = [
        'numero_pedido',
        'usuario',
        'forma_pagamento',
        'parcelas',
        'endereco',
        'criado_em',
        'atualizado_em',
    ]
    can_delete = True  # já é o valor padrão, mas pode deixar explícito

    def numero_pedido(self, obj):
        return f'{obj.id}'

    numero_pedido.short_description = 'pedido'
    numero_pedido.admin_order_field = 'id'
    numero_pedido.allow_tags = False

    def listar_itens(self, obj):
        return ', '.join(
            [
                f'{item.quantidade}x {item.produto.titulo}'
                for item in obj.itens.all()
            ]
        )

    listar_itens.short_description = 'Itens'

    def total_pedido(self, obj):
        total = sum([item.subtotal() for item in obj.itens.all()])
        return f'R$ {total:.2f}'

    total_pedido.short_description = 'TOTAL'

    def endereco_resumido(self, obj):
        return (
            (obj.endereco[:40] + '...')
            if len(obj.endereco) > 40
            else obj.endereco
        )

    endereco_resumido.short_description = 'ENDEREÇO'

    def parcelas_formatadas(self, obj):
        return obj.parcelas if obj.forma_pagamento == 'credito' else '-'

    parcelas_formatadas.short_description = 'PARCELAS'


admin.site.register(Pedido, PedidoAdmin)
