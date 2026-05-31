"""
Main application views.

Features:
- User registration and login
- PRO access control
- Search page
- Training system
- Progress tracking
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from main.decorators import pro_required
import json
from django.http import JsonResponse
from .models import UserProgress
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about_pro.html')

def pro_slova(request):
    return render(request, 'pro_slova.html')

def smart_login(request):

    # якщо вже увійшов — на головну
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')

    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


@login_required(login_url='/accounts/login/')
def get_pro(request):
    user = request.user

    # якщо користувач вже PRO → на головну
    if hasattr(user, 'profile') and user.profile.is_pro:
        return redirect('/')

    # інакше сторінка отримання PRO
    return render(request, 'get_pro.html')

def signup_view(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # перевірка паролів
        if password != confirm_password:
            messages.error(request, "Паролі не співпадають!")
            return redirect("signup")

        # перевірка дубліката
        if User.objects.filter(username=email).exists():
            messages.error(request, "Такий email вже зареєстрований!")
            return redirect("signup")

        # створення користувача
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        login(request, user)
        return redirect("get_pro")

    return render(request, "registration/signup.html")

@login_required
def payment(request):
    return render(request, "payment.html")

@login_required
def payment_done(request):
    return render(request, "payment_done.html")

@pro_required
def search(request):
    return render(request, "search.html")

@pro_required
def trainer(request):
    return render(request, 'trainer.html')

def get_progress(request):

    if not request.user.is_authenticated:
        return JsonResponse({"current_index": 0})

    set_name = request.GET.get("set") or "default"

    progress, _ = UserProgress.objects.get_or_create(
        user=request.user,
        set_name=set_name
    )

    return JsonResponse({
        "current_index": progress.current_index
    })

def save_progress(request):

    if not request.user.is_authenticated:
        return JsonResponse({"status": "guest"})

    data = json.loads(request.body)

    progress, _ = UserProgress.objects.get_or_create(
        user=request.user,
        set_name=data.get("set", "default")
    )

    progress.current_index = data["current_index"]
    progress.save()

    return JsonResponse({"status": "ok"})
