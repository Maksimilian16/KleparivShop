from .JWT_OP import create_access_token, VerifyToken
from .models import CustomUser, Product
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from base64 import b64encode
from django.core.exceptions import ObjectDoesNotExist


def create_user(request):
    phone = request.POST.get('phone', '')
    name = request.POST.get('name', '')
    password = request.POST.get('password', '')
    try:
        obj = CustomUser.objects.get(phone_number=phone)
    except ObjectDoesNotExist:
        obj = None

    if obj is not None:
        return JsonResponse({'message': 'This phone is already owned'})
    else:
        user = CustomUser(phone_number=phone, name=name, password=password)
        user.save()
        request.session['login'] = create_access_token({'user': phone})
        return JsonResponse({'message': 'Account created'})


def login_user(request):
    phone = request.POST.get('phone', '')
    password = request.POST.get('password', '')
    user = CustomUser.objects.get(phone_number=phone, password=password)
    if user:
        user_token = create_access_token({'user': phone})
        request.session['login'] = str(user_token)
    else:
        return "that`s wrong information"


def product_register(request):
    description = request.POST.get('description', '')
    name = request.POST.get('name', '')
    price = request.POST.get('price', '')
    photo = request.FILES['photo'].read()
    user = VerifyToken(request.session.get('login')).verify()
    product = Product.objects.create(
        name=name,
        description=description,
        price=price,
        author=CustomUser.objects.get(phone_number=user["user"]),
        image=photo
    )
    product.save()
    return JsonResponse({'message': 'Product created'})


def product_page(prod_id):
    x = get_object_or_404(Product, id=prod_id, visible=True)
    photo = b64encode(x.image).decode('utf-8')
    if x:
        return {'product': x, 'image': photo, 'photo_name': x.name}
    if photo is not None:
        return {'product': x, 'image': photo, 'photo_name': 'there is no photo'}


def user_page(request, user_id):
    obj = get_object_or_404(CustomUser, id=user_id)
    products = obj.products.filter(visible=True)
    editable = "edit" if user_id == VerifyToken(request.session.get('login')).verify()['user'] else None
    for product in products:
        product.encoded_image = b64encode(product.image).decode('utf-8')
    return {"name": obj.name, "phone": obj.phone_number, "products": products, 'editable': editable}


def products_show(prod_id):
    products = Product.objects.all()
    for product in products:
        product.encoded_image = b64encode(product.image).decode('utf-8')
    return products


def edit(request, id_):
    product = get_object_or_404(Product, id=id_)
    match product.visible:
        case True:
            product.visible = False
        case False:
            product.visible = True
    product.save()
    return "product edited"
