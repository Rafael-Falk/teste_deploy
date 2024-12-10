from django.urls import path
from . import views



urlpatterns = [
    path('ativo/', views.ativos, name='produto_list'),
    path('inativo/', views.inativos, name='produto_inativo'),
    path('reativo/', views.produto_inativo, name='inativo_list'),
    path('reativo/<int:pk>/', views.reativos, name='produto_reativo'),
]
