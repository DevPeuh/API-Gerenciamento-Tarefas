from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa, Tag
from .forms import AdicionarTarefa, EditarTarefaForm, TagForm

def tarefas_pendentes_list(request):
    # Filtra as tarefas no banco de dados onde o status é 'pendente'
    tarefas_pendentes = Tarefa.objects.filter(status='Pendente') 

    if request.method == 'POST':

        form = AdicionarTarefa(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas_pendentes_list') # Redireciona para a lista de tarefas pendentes
        
    else:
        form = AdicionarTarefa() # Inicializa um formulário vazio para GET requests

    # Renderiza o template com as tarefas pendentes e o formulário
    return render(request, 'app_tarefas/tarefas_pendentes.html', {'tarefas_pendentes':tarefas_pendentes, 'form': form}) 

def concluir_tarefa(request, tarefa_id):
    # Obtém a tarefa com o ID fornecido ou retorna um erro 404 se não for encontrada
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'Concluído'
    tarefa.save()

    return redirect('tarefas_pendentes_list')

def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.delete()
    return redirect('tarefas_pendentes_list')

def adiar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'Adiado'
    tarefa.save()
    return redirect('tarefas_pendentes_list')

def editar_tarefa(request, tarefa_id):
    """Edita uma tarefa existente."""
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        form = EditarTarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('tarefas_pendentes_list')
    else:
        form = EditarTarefaForm(instance=tarefa)

    return render(request, 'app_tarefas/editar_tarefa.html', {'tarefa': tarefa, 'form': form})


def tarefas_concluidas_list(request):
    tarefas_concluidas = Tarefa.objects.filter(status='Concluído')
    return render(request, 'app_tarefas/tarefas_concluidas.html', {'tarefas_concluidas':tarefas_concluidas})

def tarefas_adiadas_list(request):
    tarefas_adiadas = Tarefa.objects.filter(status='Adiado')
    return render(request, 'app_tarefas/tarefas_adiadas.html', {'tarefas_adiadas': tarefas_adiadas})

def mover_para_tarefas(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'Pendente'
    tarefa.save()
    return redirect('tarefas_pendentes_list')

def criar_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas_pendentes_list')
    else:
        form = TagForm()
    return render(request, 'app_tarefas/criar_tag.html', {'form': form})

def excluir_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    if request.method == 'POST':
        tag.delete()
        return redirect('tarefas_pendentes_list')
    return render(request, 'app_tarefas/excluir_tag.html', {'tag': tag})

def listar_tags(request):
    tags = Tag.objects.all()
    return render(request, 'app_tarefas/listar_tags.html', {'tags': tags})