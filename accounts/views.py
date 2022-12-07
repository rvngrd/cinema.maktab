from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # successful login
            login(request, user)
            return HttpResponseRedirect(reverse('ticketing:showtime_list'))
        else:
            # undefined user or wrong password
            context = {
                'username': username,
                'error': 'کاربری با این مشخصات یافت نشد'
            }
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('ticketing:showtime_list'))
        context = {}
    return render(request, 'accounts/login.html', {})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))
