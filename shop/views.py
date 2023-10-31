from django.shortcuts import render
from django.http import HttpResponse
from .JWT_OP import VerifyToken
from .BL import create_user, login_user, product_register, product_page, user_page, products_show, edit
from .forms import Products
from .models import Product


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
    return render(request, 'user.html', user_page(request, user_id))


# зробити ссилку, щоб можна було переходити на товар та шукати товари
def products_view(request):
    return render(request, 'main.html', {"products": products_show(request)})


def test(request):
    session_value = request.session.get('login')
    if session_value:
        return HttpResponse(session_value)
    else:
        request.session['my_session'] = 'Hello, World'
        return HttpResponse("Сеанс установлен")


def edit_product(request, prod_id):
    session = VerifyToken(request.session.get('login')).verify()['user']
    if session != Product.objects.get(id=prod_id).author.phone_number:
        return HttpResponse("you are not owner of this product")
    if request.POST:
        return HttpResponse(edit(request, prod_id))
    return render(request, 'edit.html')

