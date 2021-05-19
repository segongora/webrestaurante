from django.urls import path
from . import views
from .views import SalsaTemplateView, SalsaCreatePedido, PedidoSuccess, realizar_pedido

salsas_patterns = ([
    #path('', views.blog, name="blog"),
    path('create_pedido/', SalsaCreatePedido.as_view(), name='create_pedido'),
    path('success_pedido/', PedidoSuccess.as_view(), name='success_pedido'),
  # path('', RecipesListView.as_view(), name='recipes'),
    path('pedido/', views.realizar_pedido, name='detalle_pedido'),
    path('', SalsaTemplateView.as_view(), name="salsas"),
    #path('category/<int:category_id>', views.category, name="category"),
],'salsas')