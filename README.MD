# API para Gerenciamento de Tarefas

## Descrição
Este projeto é uma API para gerenciamento de tarefas, desenvolvida com Django. A API permite criar, ler, atualizar e deletar tarefas, além de gerenciar tags associadas às tarefas.

## Funcionalidades
- Criação de novas tarefas
- Leitura de tarefas existentes
- Atualização de tarefas
- Exclusão de tarefas
- Autenticação de usuários
- Gerenciamento de tags

## Acesso ao Projeto
Para acessar o projeto, você pode clonar o repositório usando o seguinte comando:
```bash
git clone https://github.com/DevPeuh/API-site-Gerenciamento-Tarefas.git
```

## Tecnologias Utilizadas
- Python
- Django
- SQLite3
- HTML/CSS para templates

## Como Usar
1. Clone o repositório
2. Instale as dependências com `pip install -r requirements.txt`
3. Configure as variáveis de ambiente
4. Aplique as migrações com `python manage.py makemigrations` e `python manage.py migrate`
5. Inicie o servidor com `python manage.py runserver`

## Endpoints
Aqui estão os principais endpoints da API:

- `GET /` - Lista todas as tarefas pendentes
- `POST /tarefas/<int:tarefa_id>/concluir/` - Conclui uma tarefa
- `POST /tarefas/<int:tarefa_id>/excluir/` - Exclui uma tarefa
- `POST /tarefas/<int:tarefa_id>/adiar/` - Adia uma tarefa
- `POST /tarefas/<int:tarefa_id>/editar/` - Edita uma tarefa
- `GET /concluidas/` - Lista todas as tarefas concluídas
- `GET /adiadas/` - Lista todas as tarefas adiadas
- `POST /tarefas/<int:tarefa_id>/mover-para-lista-de-tarefas/` - Move uma tarefa para a lista de pendentes
- `POST /criar_tag/` - Cria uma nova tag
- `POST /excluir_tag/<int:tag_id>/` - Exclui uma tag
- `GET /listar_tags/` - Lista todas as tags

## tela inicial da API
![Tela inicial da API](https://github.com/DevPeuh/API-Gerenciamento-Tarefas/blob/master/img/img-API-1.png?raw=true)
## Concluir, excluir, adiar ou editar/vizualização descritiva da tarefa
![Parte de editar, concluir, adiar ou excluir, também visualização descritiva da tarefa](https://github.com/DevPeuh/API-Gerenciamento-Tarefas/blob/master/img/img-API-2.png?raw=true)
## Por dentro da edição da tarefa
![Por dentro da edição de tarefa](https://github.com/DevPeuh/API-Gerenciamento-Tarefas/blob/master/img/img-API-3.png?raw=true)
