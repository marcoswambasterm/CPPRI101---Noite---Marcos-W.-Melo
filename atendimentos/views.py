from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Atendimento
from .forms import AtendimentoForm
from django.urls import reverse_lazy

class AtendimentoListView(ListView):
    model = Atendimento
    template_name = 'atendimento_list.html'
    context_object_name = 'atendimentos'

class AtendimentoCreateView(CreateView):
    model = Atendimento
    form_class = AtendimentoForm
    template_name = 'atendimento_form.html'
    success_url = reverse_lazy('atendimento_list')

class AtendimentoUpdateView(UpdateView):
    model = Atendimento
    form_class = AtendimentoForm
    template_name = 'atendimento_form.html'
    success_url = reverse_lazy('atendimento_list')

class AtendimentoDeleteView(DeleteView):
    model = Atendimento
    template_name = 'atendimento_confirm_delete.html'
    success_url = reverse_lazy('atendimento_list')
