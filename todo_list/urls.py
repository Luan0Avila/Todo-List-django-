from . import views
from django.urls import path

app_name = 'todo_list'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create/', views.CreateTodoView.as_view(), name='create_todo'),
]
