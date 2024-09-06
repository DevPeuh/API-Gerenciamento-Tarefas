from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.tarefas_pendentes_list, name='tarefas_pendentes_list'),
    path('tarefas/<int:tarefa_id>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),
    path('tarefas/<int:tarefa_id>/excluir/', views.excluir_tarefa, name='excluir_tarefa'),
    path('tarefas/<int:tarefa_id>/adiar/', views.adiar_tarefa, name='adiar_tarefa'),
    path('tarefas/<int:tarefa_id>/editar/', views.editar_tarefa, name='editar_tarefa'),
    path('concluidas/', views.tarefas_concluidas_list, name='tarefas_concluidas_list'),
    path('adiadas/', views.tarefas_adiadas_list, name='tarefas_adiadas_list'),
    path('tarefas/<int:tarefa_id>/mover-para-lista-de-tarefas/', views.mover_para_tarefas, name='mover_para_tarefas'),
    path('criar_tag/', views.criar_tag, name='criar_tag'),
    path('excluir_tag/<int:tag_id>/', views.excluir_tag, name='excluir_tag'),
    path('listar_tags/', views.listar_tags, name='listar_tags'),
]
