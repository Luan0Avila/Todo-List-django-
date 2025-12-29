from ..forms import RegisterForm, LoginForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from ..tokens import account_activation_token

def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'user/pages/register.html', {
            'form' : form,
            'form_action' : reverse('user:register_create')
    })

def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.is_active = False
        user.save()
        current_site = get_current_site(request)

        mail_subject = 'Ative sua conta'
        message = render_to_string(
            'user/emails/activation_email.html',
            {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            }
        )

        email = EmailMessage(
            mail_subject,
            message,
            to=[user.email]
        )
        email.send()
        messages.success(request, 'Conta criada! Verifique seu e-mail para ativá-la.')

        del(request.session['register_form_data'])
        return redirect(reverse('user:login_view'))
    
    return render(
        request,
        'user/pages/register.html',
        {
            'form': form,
            'form_action': reverse('user:register_create')
        }
    )

def activate_user(request,uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (User.DoesNotExist, ValueError, TypeError):
        user = None

    if user and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        return HttpResponse('Conta ativada com sucesso! Você já pode fazer login.')
    
    return HttpResponse('Link inválido ou expirado.')


def login_view(request):
    form  = LoginForm()
    
    return render(request, 'user/pages/login.html',{
        'form': form,
        'form_action': reverse('user:login_create')
    })

def login_create(request):
    if request.method != 'POST':
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            login(request, authenticated_user)
            messages.success(request, 'Você está conectado.')
            return redirect(reverse('todo_list:home'))

        messages.error(request, 'Invalid credentials')

    else:
        messages.error(request, 'Invalid username or password')

    return render(
        request,
        'user/pages/login.html',
        {
            'form': form,
            'form_action': reverse('user:login_create')
        }
    )

@login_required(login_url='user:login_view', redirect_field_name='next')
def logout_view(request):
    if request.method != 'POST':
        messages.error(request, 'Requisição inválida.')
        return redirect(reverse('todo_list:home'))

    if request.POST.get('username') != request.user.username:
        messages.error(request, 'Logout de usuário inválido.')
        return redirect(reverse('todo_list:home'))

    logout(request)
    messages.success(request, 'Deslogado com sucesso.')
    return redirect(reverse('user:login_view'))