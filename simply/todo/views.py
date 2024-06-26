from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    
    context = {'form': form}
    return render(request, 'my-login.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')

def user_logout(request):
    logout(request)
    return redirect('homepage')
