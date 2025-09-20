from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def register_view(request):
    """Веб-сторінка реєстрації"""
    if request.user.is_authenticated:
        return redirect('/api/auth/dashboard/')
    return render(request, 'auth/register.html')


def login_view(request):
    """Веб-сторінка входу"""
    if request.user.is_authenticated:
        return redirect('/api/auth/dashboard/')
    return render(request, 'auth/login.html')


@login_required
def dashboard_view(request):
    """Дашборд користувача"""
    return render(request, 'dashboard.html')


@login_required
def logout_view(request):
    """Вихід користувача"""
    logout(request)
    # Очищаємо JWT токени через JavaScript
    return render(request, 'auth/logout.html')


def home_view(request):
    """Головна сторінка"""
    if request.user.is_authenticated:
        return redirect('/api/auth/dashboard/')
    return redirect('/api/auth/login/')
