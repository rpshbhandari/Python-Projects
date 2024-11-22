from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models

# Create your views here.

def home(request) -> HttpResponse:
    return render(request, './home.html')

def login(request) -> HttpResponse:
    return render(request, './login.html')

def signup(request) -> HttpResponse:
    return render(request, './signup.html')

def quiz(request) -> HttpResponse:
    quiz_list = models.Quiz.objects.all()
    return render(request, './quiz_list.html', {'quiz_list': quiz_list})