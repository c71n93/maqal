"""Views for maqal application."""
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from . import proverbs_db

def index_view(request):
    """Renders the main index page. Also displays all proverbs."""
    proverbs = proverbs_db.all_proverbs()
    return render(request, "index.html", context={"proverbs": proverbs})

def login_view(request):
    """User login page."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    """User register page."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): # TODO: validate, that username length is [3, 30]
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    """Logout action"""
    logout(request)
    return index_view(request)
