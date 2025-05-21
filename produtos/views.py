from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from produtos.forms import ProdModelForm
from produtos.models import Produto, ProdutoInventario

# filtra usuarios administrador para usar no decorator
admin_required = user_passes_test(
    lambda u: u.is_staff or u.is_superuser, login_url='login'
)

# view para catalogo
class ProdutosListView(ListView):
    model = Produto
    template_name = 'catalogo.html'
    context_object_name = 'produtos'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        titulo = self.request.GET.get('titulo')
        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)
        return queryset


# view para detalhes do produtos
class ProdutosDetailView(DetailView):
    model = Produto
    template_name = 'prod_detail.html'


# view para cadastrar produtos
@method_decorator(admin_required, name='dispatch')
class CadProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdModelForm
    template_name = 'cad_prod.html'
    success_url = '/catalogo/'


# view para atualizar produtos
@method_decorator(admin_required, name='dispatch')
class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdModelForm
    template_name = 'prod_update.html'

    def get_success_url(self):
        return reverse_lazy('prod_detail', kwargs={'pk': self.object.pk})


# view para deletar produtos
@method_decorator(admin_required, name='dispatch')
class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'prod_delete.html'
    success_url = '/catalogo/'


@method_decorator(admin_required, name='dispatch')
class EstoqueView(TemplateView):
    template_name = 'estoque.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Resumo do estoque (sem paginação)
        context['estoque'] = ProdutoInventario.objects.all()[:1]

        # Paginação da lista de produtos
        produtos = Produto.objects.all()
        paginator = Paginator(produtos, 15)  # Mostra 15 por página

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['produtos'] = page_obj  # produtos agora é um Page object
        context['page_obj'] = page_obj  # útil para paginação no template

        return context
