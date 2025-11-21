from django.views.generic import ListView
from ..models import Todo
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

class TodoSearchView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todo_list/pages/search.html'
    context_object_name = 'todos'
    login_url = '/user/login/'
    redirect_field_name = 'next'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return Todo.objects.filter(
            Q(tarefa__icontains=query) |
            Q(descrição__icontains=query) |
            Q(categoria__name__icontains=query),
            user=self.request.user
        )
    
    
