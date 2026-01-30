from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        # Adicionei 'ultima_atualizacao' na lista abaixo
        fields = ['cliente', 'servico', 'descricao', 'empresa', 'tecnicos', 'status', 'prazo', 'ultima_atualizacao']
        
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'servico': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'empresa': forms.Select(attrs={'class': 'form-select'}),
            'tecnicos': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'prazo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            
            # Adicionei o visual para esse campo também
            'ultima_atualizacao': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }