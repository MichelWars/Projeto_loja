from produtos.models import Produto
from produtos.forms import ProdModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


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


class ProdutosDetailView(DetailView):
    model = Produto
    template_name = 'prod_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CadProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdModelForm
    template_name = 'cad_prod.html'
    success_url = '/catalogo/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdModelForm
    template_name = 'prod_update.html'

    def get_success_url(self):
        return reverse_lazy('prod_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'prod_delete.html'
    success_url = '/catalogo/'
