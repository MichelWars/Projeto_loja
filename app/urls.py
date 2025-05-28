from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from accounts.views import login_view, logout_view, register_view
from produtos.views import EstoqueView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='produtos/catalogo/', permanent=False)),
    

    path('estoque/', EstoqueView.as_view(), name='estoque'),
    path("accounts/", include("accounts.urls")),

    path("produtos/", include("produtos.urls")),
    path("entradas/", include("entradas.urls")),
    path("carrinho/", include("carrinho.urls")),
    path("pedidos/", include("pedidos.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
