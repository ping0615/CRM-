from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, '登入成功')
            return redirect('home')
        else:
            messages.error(request, '登入失敗,請重新嘗試')
            return redirect('home')
        
    else:
        return render(request, 'website/home.html', {})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, '登出成功')
    return redirect('home')

def register_user(request):
    return render(request, 'website/register.html', {})
