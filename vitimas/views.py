from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pessoa, PET, Vitima
from .forms import PessoaForm, PetForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Listar todas as vítimas
class ListaVitimasView(PermissionRequiredMixin, ListView):
    queryset = Pessoa.objects.all()
    template_name = 'lista_vitimas.html'
    context_object_name = 'pessoas'
    permission_required = 'vitimas.view_pessoa','vitimas.view_pet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pessoas'] = Pessoa.objects.all()
        context['pets'] = PET.objects.all()
        context['total_pessoas'] = context['pessoas'].count()
        context['total_pets'] = context['pets'].count()
        context['total_vitimas'] = context['total_pessoas'] + context['total_pets']
        return context

# Criar uma nova pessoa
class CriarPessoaView(PermissionRequiredMixin, CreateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = 'form_pessoa.html'
    success_url = reverse_lazy('lista_vitimas')
    permission_required = 'vitimas.add_pessoa'

# Editar uma pessoa existente
class EditarPessoaView(PermissionRequiredMixin, UpdateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = 'form_pessoa.html'
    success_url = reverse_lazy('lista_vitimas')
    permission_required = 'vitimas.change_pessoa'

# Deletar uma pessoa
class DeletarPessoaView(PermissionRequiredMixin, DeleteView):
    model = Pessoa
    template_name = 'confirm_delete_vitimas.html'
    success_url = reverse_lazy('lista_vitimas')
    permission_required = 'vitimas.delete_pessoa'

# Criar um novo pet
class CriarPetView(PermissionRequiredMixin, CreateView):
    model = PET
    form_class = PetForm
    template_name = 'form_pet.html'
    success_url = reverse_lazy('lista_vitimas')
    permission_required = 'vitimas.add_PET'

# Editar um pet existente
class EditarPetView(PermissionRequiredMixin, UpdateView):
    model = PET
    form_class = PetForm
    template_name = 'form_pet.html'
    success_url = reverse_lazy('lista_vitimas')
    permission_required = 'vitimas.change_PET'

# Deletar um pet
class DeletarPetView(PermissionRequiredMixin, DeleteView):
    model = PET
    template_name = 'confirm_delete_vitimas.html'
    success_url = reverse_lazy('lista_vitimas')
    permission_required = 'vitimas.delete_PET'
