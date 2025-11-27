from django import forms
from ..models import Profile  # ajuste para o caminho correto

class ProfileForm(forms.ModelForm):
    bio = forms.CharField()

    class Meta:
        model = Profile
        fields = ['bio'] 