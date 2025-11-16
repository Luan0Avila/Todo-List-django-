from django.views.generic import ListView
from ..models import Todo
from django.http import Http404

class HomeView(ListView):
    model = Todo
    template_name = 'todo_list/pages/home.html'
    context_object_name = 'todos'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Todo.objects.filter(user=self.request.user).order_by('-id')
        return super().get_queryset()
    