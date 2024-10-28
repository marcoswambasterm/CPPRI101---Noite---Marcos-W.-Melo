from django.shortcuts import render, get_object_or_404, redirect
from .models import Medico, Psicologo, Veterinario, Atendente
from .forms import MedicoForm, PsicologoForm, VeterinarioForm, AtendenteForm

# Create your views here.

def listar_medicos(request):
    medicos = Medico.objects.all()
    return render(request, './lista_medicos.html', {'medicos': medicos})

def adicionar_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_medicos')
    else:
        form = MedicoForm()
    return render(request, './form_medico.html', {'form': form})

def editar_medico(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('listar_medicos')
    else:
        form = MedicoForm(instance=medico)
    return render(request, './form_medico.html', {'form': form})

def excluir_medico(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    medico.delete()
    return redirect('listar_medicos')