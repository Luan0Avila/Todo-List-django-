from rest_framework import serializers
from .models import Todo

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','tarefa','descrição','status','categoria','user']