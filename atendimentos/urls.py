from django.urls import path
from .views import AtendimentoListView, AtendimentoCreateView, AtendimentoUpdateView, AtendimentoDeleteView


urlpatterns = [
    path('', AtendimentoListView.as_view(), name='atendimento_list'),
    path('create/', AtendimentoCreateView.as_view(), name='atendimento_create'),
    path('update/<int:pk>/', AtendimentoUpdateView.as_view(), name='atendimento_update'),
    path('delete/<int:pk>/', AtendimentoDeleteView.as_view(), name='atendimento_delete'),
]
