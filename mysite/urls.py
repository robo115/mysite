"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from store.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("shop/", include("store.url", namespace="shop")),
    path("cart/", cart, name="cart"),
    path("add_to_cart/<int:product_id>", add_to_cart, name="add_to_cart"),
    path("quantity_plus/<int:product_id>", quantity_plus, name="quantity_plus"),
    path("quantity_minus<int:product_id>", quantity_minus, name="quantity_minus"),
    path("cart_delete/<int:product_id>", cart_delete, name="cart_delete"),
    path("chekout/", checkout, name="checkout"),
    path("contact", contact, name="contact"),
    path("user/", include("users.urls"), name="user"),
    path("404/", error, name="error"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
