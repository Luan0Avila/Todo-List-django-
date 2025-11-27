from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from user.models import Profile
from django.http import HttpResponseForbidden

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