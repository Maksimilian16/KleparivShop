from django.shortcuts import render
from django.http import HttpResponse
from .BL import create_user, login_user, product_register, product_page


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


def product_register_view(request):
    if request.method == 'POST':
        return HttpResponse(product_register(request))
    return render(request, 'create_product.html')


def product_view(request, prod_id):
    return HttpResponse(product_page(prod_id))