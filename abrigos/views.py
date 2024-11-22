from operator import truediv

from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import AbrigoForm
from .models import Abrigo
# Create your views here.


# Listar Abrigos
class ListaAbrigosView(ListView):
    model = Abrigo
    template_name = 'lista_abrigos.html'
    context_object_name = 'abrigos'

# Adicionar Abrigo
class AdicionarAbrigoView(SuccessMessageMixin, CreateView):
    model = Abrigo
    template_name = 'formulario_abrigo.html'
    form_class = AbrigoForm
    success_url = reverse_lazy('listar_abrigos')
    sucess_message = 'Adicionado com sucesso!'

# Editar Abrigo
class EditarAbrigoView(UpdateView):
    model = Abrigo
    template_name = 'formulario_abrigo.html'
    fields = ['nome', 'endereco', 'capacidade', 'telefone', 'email']
    success_url = reverse_lazy('listar_abrigos')

# Excluir Abrigo
class ExcluirAbrigoView(DeleteView):
    model = Abrigo
    template_name = 'confirm_delete_abrigo.html'
    success_url = reverse_lazy('listar_abrigos')
