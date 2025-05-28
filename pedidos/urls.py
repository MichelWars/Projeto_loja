from django.urls import path
from . import views

urlpatterns = [
    
        path('finalizar_pedido/', views.finalizar_pedido, name='finalizar_pedido'),
        path('ver_pedido/<int:pk>/', views.VerPedidoView.as_view(), name='ver_pedido'),


]