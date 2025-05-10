from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from . import models, forms
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator

#filtra usuarios administrador para usar no decorator
admin_required = user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='login')


@method_decorator(admin_required, name='dispatch')
class EntradaCreateView(CreateView):
    model = models.Entrada
    template_name = 'entrada_create.html'
    form_class = forms.EntradaForm
    success_url = reverse_lazy('entrada_historico')

@method_decorator(admin_required, name='dispatch')
class EntradaListView(ListView):
    model = models.Entrada
    template_name = 'entrada.html'
    context_object_name = 'entradas'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        produto = self.request.GET.get('produto')

        if produto:
            queryset = queryset.filter(produto__titulo__icontains=produto) # navega dentro da model produto até o campo title
        
        return queryset
    
