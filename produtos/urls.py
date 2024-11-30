from django.urls import path
from produtos.views import *

urlpatterns = [
    path('', ListarProdutos.as_view(), name='listar-produtos'),
    path('novo/', CriarProdutos.as_view(), name='novo-produtos'),
    path('edit/<int:pk>/', EditarProdutos.as_view(), name='editar-produtos'),
    path('delete/<int:pk>/', DeletarProdutos.as_view(), name='deletar-produtos'),
    path('fotos/<str:arquivo>/', FotoProdutos.as_view(), name='fotos-produtos'),
    # API urls
    path('api/', APIListarProdutos.as_view(), name='api-listar-produtos'),
    path('delete/<int:pk>/', APIDeletarProdutos.as_view(), name='api-deletar-produtos'),
    path('criar/', APICriarProdutos.as_view(), name='api-criar-produto'),
    path('editar/<int:pk>/', APIEditarProdutos.as_view(), name='api-editar-produto'),

]

