from django.contrib import admin

from .models import Tarefa, Tag


# Para mostrar como tabelas determinadas na page
@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'criacao', 'prioridade', 'status', 'data_vencimento')
    search_fields = ('descricao', 'status', 'tags__nome')
    list_filter = ('status', 'prioridade', 'data_vencimento')
    filter_horizontal = ('tags',)
    fields = ('descricao', 'status', 'prioridade', 'data_vencimento', 'comentarios', 'anexos', 'tags')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('nome',)