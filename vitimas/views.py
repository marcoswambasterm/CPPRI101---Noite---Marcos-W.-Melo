from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pessoa, PET, Vitima
from .forms import PessoaForm, PetForm

# Listar todas as vítimas
class ListaVitimasView(ListView):
    queryset = Pessoa.objects.all()
    template_name = 'lista_vitimas.html'
    context_object_name = 'pessoas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pessoas'] = Pessoa.objects.all()
        context['pets'] = PET.objects.all()
        context['total_pessoas'] = context['pessoas'].count()
        context['total_pets'] = context['pets'].count()
        context['total_vitimas'] = context['total_pessoas'] + context['total_pets']
        return context

# Criar uma nova pessoa
class CriarPessoaView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = 'form_pessoa.html'
    success_url = reverse_lazy('lista_vitimas')

# Editar uma pessoa existente
class EditarPessoaView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = 'form_pessoa.html'
    success_url = reverse_lazy('lista_vitimas')

# Deletar uma pessoa
class DeletarPessoaView(DeleteView):
    model = Pessoa
    template_name = 'confirm_delete_vitimas.html'
    success_url = reverse_lazy('lista_vitimas')

# Criar um novo pet
class CriarPetView(CreateView):
    model = PET
    form_class = PetForm
    template_name = 'form_pet.html'
    success_url = reverse_lazy('lista_vitimas')

# Editar um pet existente
class EditarPetView(UpdateView):
    model = PET
    form_class = PetForm
    template_name = 'form_pet.html'
    success_url = reverse_lazy('lista_vitimas')

# Deletar um pet
class DeletarPetView(DeleteView):
    model = PET
    template_name = 'confirm_delete_vitimas.html'
    success_url = reverse_lazy('lista_vitimas')
