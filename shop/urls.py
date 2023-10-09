"""
URL configuration for KleparivShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from shop.admin import admin
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("user/register", views.user_creating, name="user_creating"),
    path("user/login", views.login, name="login"),
    path("user/<int:user_id>", views.user_view, name="user_view"),
    path("products/register", views.product_register_view, name="product_register"),
    path("products/<int:prod_id>", views.product_view, name="product_view"),
    path("products/", views.products_view, name="products_show"),
]
