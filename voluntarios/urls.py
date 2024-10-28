from django.urls import path
from . import views

urlpatterns = [
    path('medicos/', views.listar_medicos, name='listar_medicos'),
    path('medicos/adicionar/', views.adicionar_medico, name='adicionar_medico'),
    path('medicos/editar/<int:pk>/', views.editar_medico, name='editar_medico'),
    path('medicos/excluir/<int:pk>/', views.excluir_medico, name='excluir_medico'),
    # URLs para Psicologos
    path('psicologos/', views.listar_psicologos, name='listar_psicologos'),
    path('psicologos/adicionar/', views.adicionar_psicologo, name='adicionar_psicologo'),
    path('psicologos/editar/<int:pk>/', views.editar_psicologo, name='editar_psicologo'),
    path('psicologos/excluir/<int:pk>/', views.excluir_psicologo, name='excluir_psicologo'),
    # URLs para Veterinarios
    path('veterinarios/', views.listar_veterinarios, name='listar_veterinarios'),
    path('veterinarios/adicionar/', views.adicionar_veterinario, name='adicionar_veterinario'),
    path('veterinarios/editar/<int:pk>/', views.editar_veterinario, name='editar_veterinario'),
    path('veterinarios/excluir/<int:pk>/', views.excluir_veterinario, name='excluir_veterinario'),
    # URLs para Atendentes
    path('atendentes/', views.listar_atendentes, name='listar_atendentes'),
    path('atendentes/adicionar/', views.adicionar_atendente, name='adicionar_atendente'),
    path('atendentes/editar/<int:pk>/', views.editar_atendente, name='editar_atendente'),
    path('atendentes/excluir/<int:pk>/', views.excluir_atendente, name='excluir_atendente'),
]
