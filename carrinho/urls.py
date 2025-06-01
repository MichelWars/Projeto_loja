from django.urls import path

from . import views

urlpatterns = [
    path(
        'adicionar/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'
    ),
    path('ver/', views.ver_carrinho, name='ver_carrinho'),
    path('atualizar/', views.atualizar_carrinho, name='atualizar_carrinho'),
    path('remover/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path(
        'total-itens/', views.total_itens_carrinho, name='total_itens_carrinho'
    ),
]
