from django.db import models
from django.contrib.auth.models import User
class Todo(models.Model):

    class Status(models.TextChoices):
        PENDENTE = 'Pendente'
        FINALIZADO = 'Finalizado'

    tarefa = models.CharField(max_length=65, verbose_name='Titulo da tarefa')
    descrição = models.CharField(max_length=165, verbose_name='Descrição da tarefa')
    status = models.CharField(choices=Status.choices, default=Status.PENDENTE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Retorna uma representação da stirng do modelo"""
        return f"{self.descrição[:50]}..."
