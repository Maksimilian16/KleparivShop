from KleparivShop.settings import JWT_AUTH
from django.http import JsonResponse
from .JWT_OP import create_access_token
from .models import User
import jwt


def create_user(request):
    phone = request.POST.get('phone', '')
    name = request.POST.get('name', '')
    password = request.POST.get('password', '')
    if User.objects.filter(phone_number=phone).exists() or phone is not int:
        return JsonResponse({'message': 'This phone is already owned'})
    else:
        user = User(phone_number=phone, name=name, password=password)
        user.save()
        return JsonResponse({'message': 'Account created',
                             'jwt_code': str(create_access_token({'phone':phone}))})


def login_user(request):
    phone = request.POST.get('phone', '')
    password = request.POST.get('password', '')
    if User.objects.filter(phone_number=phone, password=password).exists():
        return create_access_token({'phone': phone})
    else:
        return "that`s wrong information"
