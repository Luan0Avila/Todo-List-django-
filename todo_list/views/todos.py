from django.views.generic import CreateView
from ..forms import TodoForm

class CreateTodoView(CreateView):
    template_name = 'todo_list/pages/create_todo.html'
    form_class = TodoForm
    success_url = '/'