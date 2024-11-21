from . import views
from django.urls import path
from .views import ListaAbrigosView, AdicionarAbrigoView, EditarAbrigoView, ExcluirAbrigoView

urlpatterns = [
    path('', views.ListaAbrigosView.as_view(), name='listar_abrigos'),
    path('adicionar/', views.AdicionarAbrigoView.as_view(), name='adicionar_abrigo'),
    path('<int:pk>/editar/', views.EditarAbrigoView.as_view(), name='editar_abrigo'),
    path('<int:pk>/excluir/', views.ExcluirAbrigoView.as_view(), name='excluir_abrigo'),
]
