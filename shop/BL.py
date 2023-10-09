from .JWT_OP import create_access_token, verify_token
from .models import User, Product
from django.http import JsonResponse
from .forms import Products
from django.shortcuts import get_object_or_404
from base64 import b64encode


def create_user(request):
    phone = request.POST.get('phone', '')
    name = request.POST.get('name', '')
    password = request.POST.get('password', '')
    if User.objects.filter(phone_number=phone).exists():
        return JsonResponse({'message': 'This phone is already owned'})
    else:
        user = User(phone_number=phone, name=name, password=password)
        user.save()
        return JsonResponse({'message': 'Account created',
                             'jwt_code': str(create_access_token({'phone':phone}))})


def login_user(request):
    phone = request.POST.get('phone', '')
    password = request.POST.get('password', '')
    if User.objects.filter(phone_number=phone, password=password).exists() is not None:
        return create_access_token({'phone': phone})
    else:
        return "that`s wrong information"


def product_register(request):
    form = Products(request.POST, request.FILES)
    description = request.POST.get('description', '')
    name = request.POST.get('name', '')
    price = request.POST.get('price', '')
    photo = request.FILES['photo'].read()
    user_phone_number = verify_token(request.POST.get('phone_number', ''))

    try:
        author = User.objects.get(phone_number=user_phone_number['phone'])
    except User.DoesNotExist:
        return JsonResponse({'message': 'User not found'})
    product = Product.objects.create(
        name=name,
        description=description,
        price=price,
        author=author,
        image=photo
    )
    product.save()
    return JsonResponse({'message': 'Product created'})


def product_page(prod_id):
    x = get_object_or_404(Product, id=prod_id)
    photo = b64encode(x.image).decode('utf-8')
    if x:
        return {'product': x, 'image': photo, 'photo_name': x.name}
    if photo is not None:
        return {'product': x, 'image': photo, 'photo_name': 'there is no photo'}


def user_page(user_id):
    obj = get_object_or_404(User, id=user_id)
    return f"name: {obj.name}\n phone: {obj.phone_number}\n "


def products_show(prod_id):
    return JsonResponse(Product.objects.filter(id=prod_id).values('name', 'description', 'price', 'author_id').first())
