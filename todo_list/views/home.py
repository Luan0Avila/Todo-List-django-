from django.views.generic import ListView
from ..models import Todo


class HomeView(ListView):
    model = Todo
    template_name = 'todo_list/pages/home.html'
    context_object_name = 'todo'