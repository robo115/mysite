from django.shortcuts import render
from store.models import Products, ProductsCategory
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Wishlist
from django.db.models import Sum


products = Products.objects.all()
products_all_category = ProductsCategory.objects.all()
products_vegetables = Products.objects.filter(category__name="овощи")
products_fruits = Products.objects.filter(category__name="фрукты")
products_meat = Products.objects.filter(category__name="мясо")
products_meat_count = products_meat.count()
products_fruits_count = products_fruits.count()
products_vegetables_count = products_vegetables.count()


def listing(request):
    products_list = Products.objects.all()
    paginator = Paginator(products_list, 12)

    page_number = request.GET.get("page")
    pages = paginator.page(page_number)
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "pages": pages,
    }
    return render(request, context)


def index(request):
    context = {
        "products": products,
        "products_vegetables": products_vegetables[:9],
        "products_vegetables_for_page": products_vegetables[:4],
        "products_fruits": products_fruits,
        "products_fruits_for_page": products_fruits[:4],
        "products_meat": products_meat,
        "products_category": products_all_category,
        "products_meat_count": products_meat_count,
        "products_fruits_count": products_fruits_count,
        "products_vegetables_count": products_vegetables_count,
    }
    return render(request, "store/index.html", context)


def shop(request, category_id=None):
    products_list = (
        Products.objects.filter(category_id=category_id)
        if category_id
        else Products.objects.all()
    )
    paginator = Paginator(products_list, 12)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "products_list": products_list,
        "page_obj": page_obj,
        "products_meat_count": products_meat_count,
        "products_fruits_count": products_fruits_count,
        "products_vegetables_count": products_vegetables_count,
    }
    return render(request, "store/shop.html", context)


def contact(request):
    return render(request, "store/contact-us.html")


def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Products, id=product_id)
        if product.id in Wishlist.objects.all().values_list("wished_item", flat=True):
            return redirect("cart")
        item = Wishlist(user=request.user, wished_item=product)
        item.total_product = item.quantity * product.price
        item.save()
        return redirect("index")

    else:
        return redirect('user:login')


def cart(request):
    if request.user.is_authenticated:
        items = Wishlist.objects.all()
        total_price = Wishlist.objects.all().aggregate(Sum('total_product'))['total_product__sum']
        last_price = total_price + 2
        context = {"items": items, "total_price": total_price, "last_price": last_price}
        return render(request, "store/cart.html", context)
    else:
        return redirect('user:login')


def quantity_plus(request, product_id):
    product = get_object_or_404(Wishlist, id=product_id)
    product.quantity += 1
    product.total_product = product.quantity * product.wished_item.price
    product.save()

    return redirect("cart")


def quantity_minus(request, product_id):
    product = get_object_or_404(Wishlist, id=product_id)
    product.quantity -= 1
    if product.quantity < 1:
        product.delete()
        return redirect("cart")
    product.total_product = product.quantity * product.wished_item.price
    product.save()

    return redirect("cart")


def cart_delete(request, product_id):
    product = get_object_or_404(Wishlist, id=product_id)
    product.delete()

    return redirect("cart")


def error(request, exception):
    return render(request, "store/404.html", status=404)


def checkout(request):
    if request.user.is_authenticated:
        items = Wishlist.objects.all()
        total_price = Wishlist.objects.all().aggregate(Sum('total_product'))['total_product__sum']
        last_price = total_price + 2
        context = {"items": items, "total_price": total_price, "last_price": last_price}
        return render(request, "store/checkout.html", context)
    else:
        return redirect('user:login')
