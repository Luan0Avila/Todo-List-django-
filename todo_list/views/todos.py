from django.views.generic import CreateView, UpdateView, DeleteView
from ..forms import TodoForm
from django.urls import reverse_lazy
from ..models import Todo

class CreateTodoView(CreateView):
    template_name = 'todo_list/pages/create_todo.html'
    form_class = TodoForm
    success_url = '/'

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.user = self.request.user 
        todo.save()
        return super().form_valid(form)

class UpdateTodoView(UpdateView):
    model = Todo
    fields = ['tarefa', 'descrição', 'status']
    template_name = 'todo_list/pages/update_todo.html'
    success_url = reverse_lazy('todo_list:home')


class DeleteTodoView(DeleteView):
    model = Todo
    template_name = 'todo_list/partials/delete_confirm.html'
    success_url = '/'