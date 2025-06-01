from django.urls import path

from .views import (
    CadProdutoCreateView,
    ProdutoDeleteView,
    ProdutosDetailView,
    ProdutosListView,
    ProdutoUpdateView,
)

urlpatterns = [
    path('catalogo/', ProdutosListView.as_view(), name='catalogo'),
    path('novo_produto/', CadProdutoCreateView.as_view(), name='cad_prod'),
    path(
        'produto/<int:pk>/', ProdutosDetailView.as_view(), name='prod_detail'
    ),
    path(
        'produto/<int:pk>/update/',
        ProdutoUpdateView.as_view(),
        name='prod_update',
    ),
    path(
        'produto/<int:pk>/delete/',
        ProdutoDeleteView.as_view(),
        name='prod_delete',
    ),
]
