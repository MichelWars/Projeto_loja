from django.urls import path

from .views import EntradaCreateView, EntradaListView

urlpatterns = [
    path(
        'cadastrar/',
        EntradaCreateView.as_view(),
        name='entrada_create',
    ),
    path(
        'historico/',
        EntradaListView.as_view(),
        name='entrada_historico',
    ),
]
