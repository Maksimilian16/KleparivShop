from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .BL import create_user, login_user


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def user_creating(request):
    if request.method == 'POST':
        return HttpResponse(create_user(request))
    return render(request, 'create_user.html')


def login(request):
    if request.method == 'POST':
        return HttpResponse(login_user(request))
    return render(request, 'login.html')