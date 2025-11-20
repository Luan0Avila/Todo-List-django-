from django.contrib import admin
from .models import Todo, Category

class TodoAdmin(admin.ModelAdmin):
        list_display = ('tarefa', 'descrição')

admin.site.register(Todo)
admin.site.register(Category)