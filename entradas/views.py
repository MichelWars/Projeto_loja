from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from . import forms, models

# filtra usuarios administrador para usar no decorator
admin_required = user_passes_test(
    lambda u: u.is_staff or u.is_superuser, login_url='login'
)


# view para cadastrar entradas
@method_decorator(admin_required, name='dispatch')
class EntradaCreateView(CreateView):
    model = models.Entrada
    template_name = 'entrada_create.html'
    form_class = forms.EntradaForm
    success_url = reverse_lazy('entrada_historico')

    def get_initial(self):
        initial = super().get_initial()
        produto_id = self.request.GET.get('produto_id')
        if produto_id:
            initial['produto'] = produto_id
        return initial


# Lista historico de entradas de produtos
@method_decorator(admin_required, name='dispatch')
class EntradaListView(ListView):
    model = models.Entrada
    template_name = 'entrada.html'
    context_object_name = 'entradas'
    paginate_by = 10

    # faz o filtro de pesquisa pelo produto
    def get_queryset(self):
        queryset = super().get_queryset()
        produto = self.request.GET.get('produto')

        if produto:
            queryset = queryset.filter(
                produto__titulo__icontains=produto
            )   # navega dentro da model produto até o campo title

        return queryset
