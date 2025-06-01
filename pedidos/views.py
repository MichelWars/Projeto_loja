from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView

from carrinho.carrinho import Carrinho
from produtos.models import Produto

from .forms import PedidoForm
from .models import ItemPedido, Pedido


# view para pegar produtos do carrinho e gerar pedido
@login_required
def finalizar_pedido(request):
    carrinho = Carrinho(request)
    itens_carrinho = carrinho.itens()

    if not itens_carrinho:
        return redirect('ver_carrinho')

    produtos = []
    total = 0
    estoque_insuficiente = False

    for produto_id, quantidade in itens_carrinho.items():
        produto = get_object_or_404(Produto, id=produto_id)
        # verifica se a quantidade solicitada nao excede a quantidade em estoque
        if quantidade > produto.quantidade:
            messages.error(
                request,
                f"Estoque insuficiente para o produto '{produto.titulo}'. Disponível: {produto.quantidade}, solicitado: {quantidade}.",
            )
            estoque_insuficiente = True

        subtotal = produto.valor * quantidade
        produtos.append(
            {
                'produto': produto,
                'quantidade': quantidade,
                'subtotal': subtotal,
            }
        )
        total += subtotal

    if estoque_insuficiente:
        return redirect('ver_carrinho')

    # cria o pedido
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
                    preco_unitario=item['produto'].valor,
                )

            carrinho.limpar()
            return redirect('ver_pedido', pk=pedido.pk)
    else:
        form = PedidoForm()

    return render(
        request,
        'finalizar_pedido.html',
        {
            'form': form,
            'produtos': produtos,
            'total': total,
            'parcelas': range(1, 13),
        },
    )


# view para consultar pedido individual
class VerPedidoView(LoginRequiredMixin, DetailView):
    model = Pedido
    template_name = 'ver_pedido.html'

    # controle de permissões cada usuario ve somente seus pedidos, adm ve todos
    def get_object(self, queryset=None):
        pedido = super().get_object(queryset)
        user = self.request.user
        if not user.is_superuser and pedido.usuario != user:
            raise Http404(
                'Você não tem permissão para visualizar este pedido.'
            )
        return pedido

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pedido = self.object
        itens = pedido.itens.all()
        total = sum(item.subtotal() for item in itens)

        # Valor da parcela (se aplicável)
        valor_parcela = None
        if pedido.forma_pagamento == 'credito' and pedido.parcelas:
            valor_parcela = total / pedido.parcelas

        context['itens'] = itens
        context['total'] = total
        context['valor_parcela'] = valor_parcela
        return context

    # lista de pedidos


class ListarPedidosView(LoginRequiredMixin, ListView):
    model = Pedido
    template_name = 'listar_pedidos.html'
    context_object_name = 'pedidos'
    paginate_by = 5
    ordering = ['-criado_em']

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Pedido.objects.all().order_by('-criado_em')
        return Pedido.objects.filter(usuario=self.request.user).order_by(
            '-criado_em'
        )
