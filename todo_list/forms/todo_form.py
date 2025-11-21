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
        fields = ['tarefa', 'descrição', 'status']  # categoria vem pelo input custom

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Se estiver editando (update), preencher o campo com as categorias existentes
        if self.instance.pk:
            categorias = self.instance.categoria.values_list("name", flat=True)
            self.initial['categorias_input'] = ", ".join(categorias)

    def save(self, commit=True, user=None):
        todo = super().save(commit=False)

        if user:
            todo.user = user

        if commit:
            todo.save()

        # Lê o campo do input
        categorias_texto = self.cleaned_data.get("categorias_input", "")
        categorias_nomes = [c.strip() for c in categorias_texto.split(",") if c.strip()]

        # 🔥 Remove TODAS as categorias antes de adicionar as novas
        todo.categoria.clear()

        # Recria/associa as categorias digitadas
        categorias_objs = [
            Category.objects.get_or_create(name=nome)[0]
            for nome in categorias_nomes
        ]

        if categorias_objs:
            todo.categoria.set(categorias_objs)

        return todo
