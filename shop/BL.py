from django.http import JsonResponse
from .JWT_OP import create_access_token, verify_token
from .models import User, Product
from sqlalchemy import select, text
from KleparivShop.settings import session
from django.http import JsonResponse


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
    description = request.POST.get('description', '')
    name = request.POST.get('name', '')
    price = request.POST.get('price', '')
    phone_number = request.POST.get('phone_number', '')

    # Verify the token and get the user's phone number
    user_phone_number = verify_token(phone_number)

    try:
        # Try to get the user by phone number
        author = User.objects.get(phone_number=user_phone_number['phone'])
    except User.DoesNotExist:
        # Handle the case where the user doesn't exist
        print(price, verify_token(phone_number), name)
        return JsonResponse({'message': 'User not found'})

    # Create the product with the author
    product = Product.objects.create(
        name=name,
        description=description,
        price=price,
        author=author
    )
    product.save()
    return JsonResponse({'message': 'Product created'})


def product_page(prod_id):
    product_data = (Product.objects.filter(id=prod_id).values('name', 'description', 'price', 'author_phone_number').first())
    return JsonResponse(product_data)
