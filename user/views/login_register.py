from ..forms import RegisterForm, LoginForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import Http404
from django.contrib.auth import authenticate, login

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
        user.save()
        messages.success(request, 'Your user is created, please log in')

        del(request.session['register_form_data'])
        return redirect(reverse('todo_list:home'))


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
            messages.success(request, 'Você logou.')
            return redirect(reverse('todo_list:home'))

        messages.error(request, 'Credenciais inválidas')
    else:
        messages.error(request, 'Senha ou usuário incorretos')

    # Volta para a página de login com o formulário preenchido e inválido
    return render(
        request,
        'user/pages/login.html',
        {
            'form': form,
            'form_action': reverse('user:login_create')
        }
    )