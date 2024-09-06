from django.db import models

class Tarefa(models.Model):

    # Cria os tipos de categoria status para melhor gerenciamento de tarefas
    class Prioridade(models.TextChoices):
        BAIXA = 'Baixa', 'Baixa',
        MEDIA = 'Média', 'Média',
        ALTA = 'Alta', 'Alta'

    class Status(models.TextChoices):
        PENDENTE = 'Pendente', 'Pendente',
        CONCLUIDO = 'Concluído', 'Concluído',
        ADIADO = 'Adiado', 'Adiado',


    descricao = models.CharField(max_length=350)
    criacao = models.DateTimeField(auto_now_add=True) # Para criação automática
    prioridade = models.CharField(max_length=20, choices=Prioridade.choices, default=Prioridade.MEDIA) # choices para ordem  
    status = models.CharField(max_length=25, choices=Status.choices, default=Status.PENDENTE)
    data_vencimento = models.DateField(null=True, blank=True)
    comentarios = models.TextField(blank=True)
    anexos = models.FileField(upload_to='anexos/', blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.descricao
    
    # Exibir as tarefas em uma ordem específica.
    class Meta:
        ordering = ['-criacao'] 

# Para exibir as tags e que não podem ser repetidas
class Tag(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome