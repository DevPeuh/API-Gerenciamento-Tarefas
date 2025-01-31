from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_tarefas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tarefas',
            new_name='Tarefa',
        ),
    ]
