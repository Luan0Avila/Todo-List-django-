from django.shortcuts import render

def home(request):
    return render(request, 'todo_list/home.html')

# Create your views here.
