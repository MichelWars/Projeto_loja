from produtos.models import Produto, ProdutoInventario
from produtos.forms import ProdModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render



# view para catalogo
class ProdutosListView(ListView):
    model = Produto
    template_name = 'catalogo.html'
    context_object_name = 'produtos'

    def get_queryset(self):
        produto = super().get_queryset().order_by('titulo')
        search = self.request.GET.get('search')
        if search:
            produto = produto.filter(model__icontains=search)
        return produto


# view para detalhes do produtos
class ProdutosDetailView(DetailView):
    model = Produto
    template_name = 'prod_detail.html'


# view para cadastrar produtos
@method_decorator(login_required(login_url='login'), name='dispatch')
class CadProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdModelForm
    template_name = 'cad_prod.html'
    success_url = '/catalogo/'


# view para atualizar produtos
@method_decorator(login_required(login_url='login'), name='dispatch')
class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdModelForm
    template_name = 'prod_update.html'

    def get_success_url(self):
        return reverse_lazy('prod_detail', kwargs={'pk': self.object.pk})


# view para deletar produtos
@method_decorator(login_required(login_url='login'), name='dispatch')
class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'prod_delete.html'
    success_url = '/catalogo/'



def estoque_view(request):
    contagem = ProdutoInventario.objects.values('contador_produtos', 'valor_estoque')
    return render(request, 'estoque.html', {'estoque': contagem})
