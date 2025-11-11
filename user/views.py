from django.shortcuts import render

def user(request):
    return render(request, 'user/register.html')
