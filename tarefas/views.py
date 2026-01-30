from django.shortcuts import render,redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm
from datetime import date # <--- 1. Adicione essa importação 

def lista_tarefas(request):
    # Busca todas as tarefas, ordenando pelas pendentes primeiro
    tarefas = Tarefa.objects.all().order_by('status', 'prazo')
    
    # Separa contadores para o topo da tela (Dashboard)
    total = tarefas.count()
    feitos = tarefas.filter(status='feito').count()
    pendentes = total - feitos
    
    return render(request, 'tarefas/lista.html', {
        'tarefas': tarefas,
        'total': total,
        'feitos': feitos,
        'pendentes': pendentes,
        'today': date.today()
    })

def nova_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()
    
    return render(request, 'tarefas/form_tarefa.html', {'form': form, 'titulo': 'Nova Tarefa'})

def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    
    return render(request, 'tarefas/form_tarefa.html', {'form': form, 'titulo': 'Editar Tarefa'})

def excluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect('lista_tarefas')