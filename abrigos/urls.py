from django.urls import path
from .views import ListaAbrigosView, AdicionarAbrigoView, EditarAbrigoView, ExcluirAbrigoView

urlpatterns = [
    path('', ListaAbrigosView.as_view(), name='listar_abrigos'),
    path('adicionar/', AdicionarAbrigoView.as_view(), name='adicionar_abrigo'),
    path('editar/<int:pk>/', EditarAbrigoView.as_view(), name='editar_abrigo'),
    path('excluir/<int:pk>/', ExcluirAbrigoView.as_view(), name='excluir_abrigo'),
]
