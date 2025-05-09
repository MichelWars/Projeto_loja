from produtos.models import Produto, ProdutoInventario
from produtos.forms import ProdModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django.shortcuts import render

#filtra usuarios administrador para usar no decorator
admin_required = user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='login')

# view para catalogo
class ProdutosListView(ListView):
    model = Produto
    template_name = 'catalogo.html'
    context_object_name = 'produtos'

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
# @method_decorator(login_required(login_url='login'), name='dispatch')
class CadProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdModelForm
    template_name = 'cad_prod.html'
    success_url = '/catalogo/'


# view para atualizar produtos
#@method_decorator(login_required(login_url='login'), name='dispatch')
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


# @method_decorator(admin_required, name='dispatch')
# class EstoqueView(ListView):
#     model = ProdutoInventario
#     template_name = 'estoque.html' 
#     context_object_name = 'estoque'

#     def get_queryset(self):
#         return ProdutoInventario.objects.all()[:1]

@method_decorator(admin_required, name='dispatch')
class EstoqueView(TemplateView):
    template_name = 'estoque.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Dados da tabela 1 (resumo do estoque)
        context['estoque'] = ProdutoInventario.objects.all()[:1]

        # Dados da tabela 2 (lista de produtos)
        context['produtos'] = Produto.objects.all()

        return context
