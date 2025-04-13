"""Views for maqal application."""
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .models import Proverb
from .forms import ProverbForm, MaqalUserCreationForm
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
        form = MaqalUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = MaqalUserCreationForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    """Logout action"""
    logout(request)
    return index_view(request)

@login_required
def add_proverb_view(request):
    """Add proverb action"""
    if request.method == 'POST':
        form = ProverbForm(request.POST)
        if form.is_valid():
            proverb = form.save(commit=False)
            proverb.author = request.user
            proverb.save()
            return redirect('index')
    else:
        form = ProverbForm()
    return render(request, "add_proverb.html", {'form': form})

@login_required
def profile_view(request):
    """View profile"""
    user_proverbs = Proverb.objects.filter(author=request.user).order_by('-modified_at')
    context = {
        'proverbs_count': user_proverbs.count(),
        'user_proverbs': user_proverbs,
        'user': request.user
    }
    return render(request, 'profile.html', context)
