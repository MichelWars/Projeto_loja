from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from produtos.views import ProdutosListView, CadProdutoCreateView, ProdutosDetailView, ProdutoUpdateView, ProdutoDeleteView
from accounts.views import register_view, login_view, logout_view
from produtos.views import estoque_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('catalogo/', ProdutosListView.as_view(), name='catalogo'),
    path('novo_produto/', CadProdutoCreateView.as_view(), name='cad_prod'),
    path('produto/<int:pk>/', ProdutosDetailView.as_view(), name='prod_detail'),
    path('produto/<int:pk>/update/', ProdutoUpdateView.as_view(), name='prod_update'),
    path('produto/<int:pk>/delete/', ProdutoDeleteView.as_view(), name='prod_delete'),
    path('estoque/', estoque_view, name='estoque'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
