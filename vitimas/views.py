from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa, PET
from .forms import PessoaForm, PetForm

# Create your views here.

# Listar todas as vítimas
def lista_vitimas(request):
    pessoas = Pessoa.objects.all()
    pets = PET.objects.all()
    return render(request, './lista_vitimas.html', {'pessoas': pessoas, 'pets': pets})

# Criar uma nova pessoa
def criar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vitimas')
    else:
        form = PessoaForm()
    return render(request, './form_pessoa.html', {'form': form})

# Editar uma pessoa existente
def editar_pessoa(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('lista_vitimas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, './form_pessoa.html', {'form': form})


# Deletar uma pessoa
def deletar_pessoa(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('lista_vitimas')
    return render(request, './confirm_delete.html', {'obj': pessoa})

# Criar um novo pet
def criar_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vitimas')
    else:
        form = PetForm()
    return render(request, './form_pet.html', {'form': form})

# Editar um pet existente
def editar_pet(request, pk):
    pet = get_object_or_404(PET, pk=pk)
    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('lista_vitimas')
    else:
        form = PetForm(instance=pet)
    return render(request, './form_pet.html', {'form': form})

# Deletar um pet
def deletar_pet(request, pk):
    pet = get_object_or_404(PET, pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('lista_vitimas')
    return render(request, './confirm_delete.html', {'obj': pet})

