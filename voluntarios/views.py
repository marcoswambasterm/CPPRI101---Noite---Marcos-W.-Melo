from django.shortcuts import render, get_object_or_404, redirect
from .models import Medico, Psicologo, Veterinario, Atendente
from .forms import MedicoForm, PsicologoForm, VeterinarioForm, AtendenteForm

def lista_voluntarios(request):
    # Obter a contagem de cada tipo de voluntário
    total_medicos = Medico.objects.count()
    total_psicologos = Psicologo.objects.count()
    total_veterinarios = Veterinario.objects.count()
    total_atendentes = Atendente.objects.count()
    total_voluntarios = total_medicos + total_psicologos + total_veterinarios + total_atendentes

    context = {
        'total_medicos': total_medicos,
        'total_psicologos': total_psicologos,
        'total_veterinarios': total_veterinarios,
        'total_atendentes': total_atendentes,
        'total_voluntarios': total_voluntarios,
    }
    return render(request, 'lista_voluntarios.html', context)

# Médicos
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
            return redirect('lista_medicos')
    else:
        form = MedicoForm(instance=medico)
    return render(request, './form_medico.html', {'form': form})

def excluir_medico(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == "POST":
        medico.delete()
        return redirect('listar_medicos')
    return render(request, './confirm_delete_medicos.html', {'obj': medico})

# Psicólogos
def listar_psicologos(request):
    psicologos = Psicologo.objects.all()
    return render(request, './lista_psicologos.html', {'psicologos': psicologos})

def adicionar_psicologo(request):
    if request.method == 'POST':
        form = PsicologoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_psicologos')
    else:
        form = PsicologoForm()
    return render(request, './form_psicologo.html', {'form': form})

def editar_psicologo(request, pk):
    psicologo = get_object_or_404(Psicologo, pk=pk)
    if request.method == 'POST':
        form = PsicologoForm(request.POST, instance=psicologo)
        if form.is_valid():
            form.save()
            return redirect('listar_psicologos')
    else:
        form = PsicologoForm(instance=psicologo)
    return render(request, './form_psicologo.html', {'form': form})

def excluir_psicologo(request, pk):
    psicologo = get_object_or_404(Psicologo, pk=pk)
    if request.method == "POST":
        psicologo.delete()
        return redirect('listar_psicologos')
    return render(request, './confirm_delete_psicologos.html', {'obj': psicologo})

# Veterinários
def listar_veterinarios(request):
    veterinarios = Veterinario.objects.all()
    return render(request, './lista_veterinarios.html', {'veterinarios': veterinarios})

def adicionar_veterinario(request):
    if request.method == 'POST':
        form = VeterinarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_veterinarios')
    else:
        form = VeterinarioForm()
    return render(request, './form_veterinario.html', {'form': form})

def editar_veterinario(request, pk):
    veterinario = get_object_or_404(Veterinario, pk=pk)
    if request.method == 'POST':
        form = VeterinarioForm(request.POST, instance=veterinario)
        if form.is_valid():
            form.save()
            return redirect('listar_veterinarios')
    else:
        form = VeterinarioForm(instance=veterinario)
    return render(request, './form_veterinario.html', {'form': form})

def excluir_veterinario(request, pk):
    veterinario = get_object_or_404(Veterinario, pk=pk)
    if request.method == "POST":
        veterinario.delete()
        return redirect('listar_veterinarios')
    return render(request, './confirm_delete_veterinarios.html', {'obj': veterinario})

# Atendentes
def listar_atendentes(request):
    atendentes = Atendente.objects.all()
    return render(request, './lista_atendentes.html', {'atendentes': atendentes})

def adicionar_atendente(request):
    if request.method == 'POST':
        form = AtendenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_atendentes')
    else:
        form = AtendenteForm()
    return render(request, './form_atendente.html', {'form': form})

def editar_atendente(request, pk):
    atendente = get_object_or_404(Atendente, pk=pk)
    if request.method == 'POST':
        form = AtendenteForm(request.POST, instance=atendente)
        if form.is_valid():
            form.save()
            return redirect('listar_atendentes')
    else:
        form = AtendenteForm(instance=atendente)
    return render(request, './form_atendente.html', {'form': form})

def excluir_atendente(request, pk):
    atendente = get_object_or_404(Atendente, pk=pk)
    if request.method == "POST":
        atendente.delete()
        return redirect('listar_atendentes')
    return render(request, './confirm_delete_atendentes.html', {'obj': atendente})