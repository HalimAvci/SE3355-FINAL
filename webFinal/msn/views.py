from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import User1, News1
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.

def index(request):
    return render(request, "msn/index.html")

def news(request):
    return render(request, "msn/news.html")

def news2(request):
    return render(request, "msn/news2.html")

def login(request):
    return render(request, "account/login.html")

def register(request):
    return render(request, "account/register.html")

def english(request):
    return render(request, "msn/english.html")

def english2(request):
    return render(request, "msn/english2.html")

def english3(request):
    return render(request, "msn/english3.html")

def english4(request):
    return render(request, "msn/english4.html")

def english5(request):
    return render(request, "msn/english5.html")

