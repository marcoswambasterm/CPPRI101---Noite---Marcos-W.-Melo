from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Abrigo
# Create your views here.


# Listar Abrigos
class ListaAbrigosView(ListView):
    model = Abrigo
    template_name = 'lista_abrigos.html'
    context_object_name = 'abrigos'

# Adicionar Abrigo
class AdicionarAbrigoView(CreateView):
    model = Abrigo
    template_name = 'formulario_abrigo.html'
    fields = ['nome', 'endereco', 'capacidade', 'telefone', 'email']
    success_url = reverse_lazy('listar_abrigos')

# Editar Abrigo
class EditarAbrigoView(UpdateView):
    model = Abrigo
    template_name = 'formulario_abrigo.html'
    fields = ['nome', 'endereco', 'capacidade', 'telefone', 'email']
    success_url = reverse_lazy('listar_abrigos')

# Excluir Abrigo
class ExcluirAbrigoView(DeleteView):
    model = Abrigo
    template_name = 'confirmar_exclusao_abrigo.html'
    success_url = reverse_lazy('listar_abrigos')
