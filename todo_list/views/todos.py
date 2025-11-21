from django.views.generic import CreateView, UpdateView, DeleteView,View
from ..forms import TodoForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from ..models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateTodoView(LoginRequiredMixin, CreateView):
    template_name = 'todo_list/pages/create_todo.html'
    form_class = TodoForm
    success_url = '/'

    def form_valid(self, form):
        form.save(user=self.request.user)
        return redirect(self.success_url)

class UpdateTodoView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo_list/pages/update_todo.html'
    success_url = reverse_lazy('todo_list:home')


class DeleteTodoView(DeleteView):
    model = Todo
    template_name = 'todo_list/partials/delete_confirm.html'
    success_url = '/'


class ToggleStatusView(View):
    def post(self, request, pk):
        todo = Todo.objects.get(pk=pk)

        if todo.status == Todo.Status.PENDENTE:
            todo.status = Todo.Status.FINALIZADO
        else:
            todo.status = Todo.Status.PENDENTE

        todo.save()

        return redirect('/')