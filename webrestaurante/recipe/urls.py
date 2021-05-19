from django.urls import path
from . import views
from .views import RecipesListView, RecipeDetailView, RecipesCreateView, RecipeUpdateView, RecipesDeleteView, realizar_pedido, RecipeCreatePedido, PedidoSuccess


recipe_patterns = ([
    path('create_pedido/', RecipeCreatePedido.as_view(), name='create_pedido'),
    path('success_pedido/', PedidoSuccess.as_view(), name='success_pedido'),
    path('', RecipesListView.as_view(), name='recipes'),
    path('pedido/', views.realizar_pedido, name='detalle_pedido'),
    path('<int:pk>/<slug:recipe_slug>/',
         RecipeDetailView.as_view(), name='recipe'),
    path('create/', RecipesCreateView.as_view(), name='create'),
    path('update/<int:pk>', RecipeUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', RecipesDeleteView.as_view(), name='delete')
], 'recipes')
