from ..models import Todo
from django import forms

class TodoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tarefa'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Titulo da tarefa'})
        self.fields['descrição'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Descrição da tarefa'})

    class Meta:
        model = Todo
        fields = ['tarefa', 'descrição', 'status']  

