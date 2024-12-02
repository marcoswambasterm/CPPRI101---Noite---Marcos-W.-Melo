from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Medico, Psicologo, Veterinario, Atendente, Voluntario
from .forms import MedicoForm, PsicologoForm, VeterinarioForm, AtendenteForm
from django.core.mail import send_mail

# Lista Geral de Voluntários
class ListaVoluntariosView(ListView):
    queryset = Medico.objects.all()
    template_name = 'lista_voluntarios.html'
    context_object_name = 'voluntarios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_medicos'] = Medico.objects.count()
        context['total_psicologos'] = Psicologo.objects.count()
        context['total_veterinarios'] = Veterinario.objects.count()
        context['total_atendentes'] = Atendente.objects.count()
        context['total_voluntarios'] = (
            context['total_medicos'] + context['total_psicologos'] + context['total_veterinarios'] + context['total_atendentes']
        )
        return context

# Views de Médicos
class ListaMedicosView(ListView):
    model = Medico
    template_name = 'lista_medicos.html'
    context_object_name = 'medicos'

class AdicionarMedicoView(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'form_medico.html'
    success_url = reverse_lazy('lista_medicos')

    def form_valid(self, form):
        # Enviar o e-mail quando o formulário for validado com sucesso
        response = super().form_valid(form)

        # Enviar e-mail
        subject = 'Cadastro de Médico Realizado com Sucesso'
        message = f'O médico {form.instance.nome} foi cadastrado com sucesso no sistema.'
        from_email = 'marcoswambasterm@gmail.com'
        recipient_list = [form.instance.email]

        send_mail(subject, message, from_email, recipient_list)

        return response

class EditarMedicoView(UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'form_medico.html'
    success_url = reverse_lazy('lista_medicos')

class ExcluirMedicoView(DeleteView):
    model = Medico
    template_name = 'confirm_delete_medicos.html'
    success_url = reverse_lazy('lista_medicos')

# Views de Psicólogos
class ListaPsicologosView(ListView):
    model = Psicologo
    template_name = 'lista_psicologos.html'
    context_object_name = 'psicologos'

class AdicionarPsicologoView(CreateView):
    model = Psicologo
    form_class = PsicologoForm
    template_name = 'form_psicologo.html'
    success_url = reverse_lazy('listar_psicologos')

class EditarPsicologoView(UpdateView):
    model = Psicologo
    form_class = PsicologoForm
    template_name = 'form_psicologo.html'
    success_url = reverse_lazy('listar_psicologos')

class ExcluirPsicologoView(DeleteView):
    model = Psicologo
    template_name = 'confirm_delete_psicologos.html'
    success_url = reverse_lazy('listar_psicologos')

# Views de Veterinários
class ListaVeterinariosView(ListView):
    model = Veterinario
    template_name = 'lista_veterinarios.html'
    context_object_name = 'veterinarios'

class AdicionarVeterinarioView(CreateView):
    model = Veterinario
    form_class = VeterinarioForm
    template_name = 'form_veterinario.html'
    success_url = reverse_lazy('listar_veterinarios')

class EditarVeterinarioView(UpdateView):
    model = Veterinario
    form_class = VeterinarioForm
    template_name = 'form_veterinario.html'
    success_url = reverse_lazy('listar_veterinarios')

class ExcluirVeterinarioView(DeleteView):
    model = Veterinario
    template_name = 'confirm_delete_veterinarios.html'
    success_url = reverse_lazy('listar_veterinarios')

# Views de Atendentes
class ListaAtendentesView(ListView):
    model = Atendente
    template_name = 'lista_atendentes.html'
    context_object_name = 'atendentes'

class AdicionarAtendenteView(CreateView):
    model = Atendente
    form_class = AtendenteForm
    template_name = 'form_atendente.html'
    success_url = reverse_lazy('lista_atendentes')

class EditarAtendenteView(UpdateView):
    model = Atendente
    form_class = AtendenteForm
    template_name = 'form_atendente.html'
    success_url = reverse_lazy('lista_atendentes')

class ExcluirAtendenteView(DeleteView):
    model = Atendente
    template_name = 'confirm_delete_atendentes.html'
    success_url = reverse_lazy('lista_atendentes')
