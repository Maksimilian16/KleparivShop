from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User
from .BL import create_user, login_user, product_register, product_page, user_page, products_show
from .forms import Products


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
    return render(request, 'create_product.html', {'form': Products()})


def product_view(request, prod_id):
    return render(request, 'product_page.html', product_page(prod_id))


def user_view(request, user_id):
    return HttpResponse(user_page(user_id))


#зробити ссилку, щоб можна було переходити на товар та шукати товари
def products_view(request):
    return render(request, 'main.html', {"products": products_show(request)})
