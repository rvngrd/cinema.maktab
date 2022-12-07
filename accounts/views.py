from django.contrib.auth import authenticate, login
from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            return Http404('نام کاربری یا رمز عبور اشتباه است')
        else:
            login(request, user)
            return HttpResponse('{} خوش آمدید'.format(username))
    else:
        return render(request, 'accounts/login.html', {})

def logout_view(request):
    pass