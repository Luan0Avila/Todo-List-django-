from ..models import Todo, Category
from django import forms

class TodoForm(forms.ModelForm):
    categorias_input = forms.CharField(
        required=False,
        label='Categorias',
        help_text='Separe várias categorias com vírgula',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Todo
        fields = ['tarefa', 'descrição', 'status']

    def save(self, commit=True, user=None):
        # salva o todo sem categoria ainda
        todo = super().save(commit=False)

        # define o usuário se informado
        if user:
            todo.user = user

        # precisa salvar aqui primeiro para gerar o id
        if commit:
            todo.save()

        # agora sim podemos manipular o ManyToMany
        categorias_texto = self.cleaned_data.get("categorias_input", "")
        categorias_nomes = [c.strip() for c in categorias_texto.split(",") if c.strip()]

        categorias_objs = [
            Category.objects.get_or_create(name=nome)[0]
            for nome in categorias_nomes
        ]

        # Associa categorias
        if categorias_objs:
            todo.categoria.set(categorias_objs)

        return todo
