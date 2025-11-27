from django.views.generic import TemplateView, UpdateView
from django.shortcuts import get_object_or_404
from user.models import Profile
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from ..forms import ProfileForm

class ProfileView(TemplateView):
    template_name = 'user/pages/profile.html'

    def get(self, request, *args, **kwargs):
        profile_id = kwargs.get('id')

        profile = get_object_or_404(
            Profile.objects.select_related('user'),
            pk=profile_id
        )

        if profile.user != request.user:
            return HttpResponseForbidden("Você não tem permissão para acessar este perfil.")

        return self.render_to_response({
            'profile': profile,
        })
    
class ProfileEdit(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'user/pages/edit_profile.html'
    
    def get_success_url(self):
        return reverse_lazy('user:profile', kwargs={'id': self.object.pk})