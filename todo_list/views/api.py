from rest_framework.viewsets import ModelViewSet
from ..models import Todo
from ..serializers import TodoListSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class TodoAPIVieSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoListSerializer
    http_method_names = ['get','head','options','patch','post','delete']
    permission_classes = [IsAuthenticatedOrReadOnly,]
    def get_object(self):
        pk = self.kwargs.get('pk', '')

        obj = get_object_or_404(
            self.get_queryset(),
            pk=pk,
        )

        self.check_object_permissions(self.request, obj)

        return obj