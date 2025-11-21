from . import views
from django.urls import path

app_name = 'todo_list'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create/', views.CreateTodoView.as_view(), name='create_todo'),
    path('edit/<int:pk>/', views.UpdateTodoView.as_view(), name='edit_todo'),
    path('delete/<int:pk>/', views.DeleteTodoView.as_view(), name='delete_todo'),
    path('toggle/<int:pk>/', views.ToggleStatusView.as_view(), name='toggle_status'),
    path('search/', views.TodoSearchView.as_view(), name='search_todos'),
]
