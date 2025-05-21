from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from accounts.views import login_view, logout_view, register_view
from entradas.views import EntradaCreateView, EntradaListView
from produtos.views import (CadProdutoCreateView, EstoqueView,
                            ProdutoDeleteView, ProdutosDetailView,
                            ProdutosListView, ProdutoUpdateView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='catalogo/', permanent=False)),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
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
    path('estoque/', EstoqueView.as_view(), name='estoque'),
    path(
        'cadastrar_entrada/',
        EntradaCreateView.as_view(),
        name='entrada_create',
    ),
    path(
        'historico_entrada/',
        EntradaListView.as_view(),
        name='entrada_historico',
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
