from django import forms
from .models import Tarefa, Tag

class AdicionarTarefa(forms.ModelForm):
    """Formulário para adicionar uma nova tarefa."""

    class Meta:
        model = Tarefa
        fields = ('descricao', 'prioridade')
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descrição da tarefa'}),
            'prioridade': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'descricao': 'Descrição',
            'prioridade': 'Prioridade',
        }
        help_texts = {
            'descricao': 'Insira uma descrição detalhada da tarefa',
            'prioridade': 'Selecione a prioridade da tarefa',
        }

class EditarTarefaForm(forms.ModelForm):
    """Formulário para editar uma tarefa existente."""

    class Meta:
        model = Tarefa
        fields = ('descricao', 'prioridade', 'status', 'data_vencimento', 'comentarios', 'anexos', 'tags')
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descrição da tarefa'}),
            'prioridade': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'data_vencimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'comentarios': forms.Textarea(attrs={'class': 'form-control'}),
            'anexos': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['nome']