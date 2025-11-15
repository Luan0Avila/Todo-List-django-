from django.views.generic import CreateView, UpdateView
from ..forms import TodoForm
from django.urls import reverse_lazy
from ..models import Todo

class CreateTodoView(CreateView):
    template_name = 'todo_list/pages/create_todo.html'
    form_class = TodoForm
    success_url = '/'

class UpdateTodoView(UpdateView):
    model = Todo
    fields = ['tarefa', 'descrição', 'status']
    template_name = 'todo_list/pages/update_todo.html'
    success_url = reverse_lazy('todo_list:home')