from rest_framework.viewsets import ModelViewSet
from ..models import Todo
from ..serializers import TodoListSerializer

class TodoAPIVieSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoListSerializer
    http_method_names = ['get','head','options']