from django.urls import path
from . import views

urlpatterns = [
    path('voluntarios/', views.ListaVoluntariosView.as_view(), name='lista_voluntarios'),

    # URLs para Médicos
    path('medicos/', views.ListaMedicosView.as_view(), name='lista_medicos'),
    path('medicos/adicionar/', views.AdicionarMedicoView.as_view(), name='adicionar_medico'),
    path('medicos/editar/<int:pk>/', views.EditarMedicoView.as_view(), name='editar_medico'),
    path('medicos/excluir/<int:pk>/', views.ExcluirMedicoView.as_view(), name='excluir_medico'),

    # URLs para Psicólogos
    path('psicologos/', views.ListaPsicologosView.as_view(), name='listar_psicologos'),
    path('psicologos/adicionar/', views.AdicionarPsicologoView.as_view(), name='adicionar_psicologo'),
    path('psicologos/editar/<int:pk>/', views.EditarPsicologoView.as_view(), name='editar_psicologo'),
    path('psicologos/excluir/<int:pk>/', views.ExcluirPsicologoView.as_view(), name='excluir_psicologo'),

    # URLs para Veterinários
    path('veterinarios/', views.ListaVeterinariosView.as_view(), name='listar_veterinarios'),
    path('veterinarios/adicionar/', views.AdicionarVeterinarioView.as_view(), name='adicionar_veterinario'),
    path('veterinarios/editar/<int:pk>/', views.EditarVeterinarioView.as_view(), name='editar_veterinario'),
    path('veterinarios/excluir/<int:pk>/', views.ExcluirVeterinarioView.as_view(), name='excluir_veterinario'),

    # URLs para Atendentes
    path('atendentes/', views.ListaAtendentesView.as_view(), name='lista_atendentes'),
    path('atendentes/adicionar/', views.AdicionarAtendenteView.as_view(), name='adicionar_atendente'),
    path('atendentes/editar/<int:pk>/', views.EditarAtendenteView.as_view(), name='editar_atendente'),
    path('atendentes/excluir/<int:pk>/', views.ExcluirAtendenteView.as_view(), name='excluir_atendente'),
]
