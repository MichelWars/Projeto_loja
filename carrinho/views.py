from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from produtos.models import Produto
from .carrinho import Carrinho
from django.views.decorators.http import require_POST

@require_POST
def adicionar_ao_carrinho(request):
    produto_id = request.POST.get("produto_id")
    quantidade = int(request.POST.get("quantidade", 1))
    carrinho = Carrinho(request)
    carrinho.adicionar(produto_id, quantidade)
    return JsonResponse({"total_itens": sum(carrinho.itens().values())})


# def ver_carrinho(request):
#     carrinho = Carrinho(request)
#     produtos_carrinho = []

#     for produto_id, quantidade in carrinho.itens().items():
#         produto = get_object_or_404(Produto, id=produto_id)
#         produtos_carrinho.append({
#             "produto": produto,
#             "quantidade": quantidade,
#             "subtotal": produto.valor * quantidade
#         })

#     total = sum(item["subtotal"] for item in produtos_carrinho)

#     return render(request, "ver.html", {
#         "produtos": produtos_carrinho,
#         "total": total
#     })


@require_POST
def atualizar_carrinho(request):
    produto_id = request.POST.get("produto_id")
    quantidade = int(request.POST.get("quantidade", 1))
    carrinho = Carrinho(request)
    carrinho.atualizar(produto_id, quantidade)
    return HttpResponseRedirect("/carrinho/ver/")


@require_POST
def remover_do_carrinho(request):
    produto_id = request.POST.get("produto_id")
    carrinho = Carrinho(request)
    carrinho.remover(produto_id)
    return HttpResponseRedirect("ver/")


def total_itens_carrinho(request):
    carrinho = Carrinho(request)
    total = sum(carrinho.itens().values())
    return JsonResponse({"total_itens": total})


def ver_carrinho(request):
    carrinho = Carrinho(request)
    produtos_carrinho = []

    for produto_id, quantidade in carrinho.itens().items():
        produto = get_object_or_404(Produto, id=produto_id)
        produtos_carrinho.append({
            "produto": produto,
            "quantidade": int(quantidade),
            "subtotal": produto.valor * int(quantidade)
        })

    total = sum(item["subtotal"] for item in produtos_carrinho)

    return render(request, "ver.html", {
        "produtos": produtos_carrinho,
        "total": total,
        "quantidades": range(0, 11)  # para o <select>
    })

