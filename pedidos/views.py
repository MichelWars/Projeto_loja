from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from produtos.models import Produto
from .models import Pedido, ItemPedido
from .forms import PedidoForm
from carrinho.carrinho import Carrinho

@login_required
def finalizar_pedido(request):
    carrinho = Carrinho(request)
    itens_carrinho = carrinho.itens()

    if not itens_carrinho:
        return redirect('ver_carrinho')

    produtos = []
    total = 0

    for produto_id, quantidade in itens_carrinho.items():
        produto = get_object_or_404(Produto, id=produto_id)
        subtotal = produto.valor * quantidade
        produtos.append({
            'produto': produto,
            'quantidade': quantidade,
            'subtotal': subtotal
        })
        total += subtotal

    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.usuario = request.user
            pedido.valor_total = total
            pedido.save()

            for item in produtos:
                ItemPedido.objects.create(
                    pedido=pedido,
                    produto=item['produto'],
                    quantidade=item['quantidade'],
                    preco_unitario=item['produto'].valor
                )

            carrinho.limpar()
            return redirect('confirmacao_pedido')
    else:
        form = PedidoForm()

    return render(request, 'finalizar_pedido.html', {
        'form': form,
        'produtos': produtos,
        'total': total,
        'parcelas': range(1, 13)
    })
