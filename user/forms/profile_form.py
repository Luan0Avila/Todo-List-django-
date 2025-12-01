from django import forms
from ..models import Profile

class ProfileForm(forms.ModelForm):
    bio = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'textarea-bio',
            'rows': 6,
            'placeholder': 'Escreva algo sobre você...'
        })
    )
    

    class Meta:
        model = Profile
        fields = ['bio']
