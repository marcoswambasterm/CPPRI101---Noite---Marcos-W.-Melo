from django.urls import path
from .views import (
    ListaVitimasView, CriarPessoaView, EditarPessoaView, DeletarPessoaView,
    CriarPetView, EditarPetView, DeletarPetView
)

urlpatterns = [
    path('vitimas/', ListaVitimasView.as_view(), name='lista_vitimas'),
    path('vitimas/nova-pessoa/', CriarPessoaView.as_view(), name='criar_pessoa'),
    path('editar-pessoa/<int:pk>/', EditarPessoaView.as_view(), name='editar_pessoa'),
    path('vitimas/deletar-pessoa/<int:pk>/', DeletarPessoaView.as_view(), name='deletar_pessoa'),

    path('vitimas/novo-pet/', CriarPetView.as_view(), name='criar_pet'),
    path('vitimas/editar-pet/<int:pk>/', EditarPetView.as_view(), name='editar_pet'),
    path('vitimas/deletar-pet/<int:pk>/', DeletarPetView.as_view(), name='deletar_pet'),
]
