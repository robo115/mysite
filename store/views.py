from django.shortcuts import render
from store.models import Products, ProductsCategory
from django.core.paginator import Paginator
from django.shortcuts import render

products = Products.objects.all()
products_all_category = ProductsCategory.objects.all()
products_vegetables = Products.objects.filter(category__name='овощи')
products_fruits = Products.objects.filter(category__name='фрукты')
products_meat = Products.objects.filter(category__name='мясо')
products_meat_count = products_meat.count()
products_fruits_count = products_fruits.count()
products_vegetables_count = products_vegetables.count()


def listing(request):
    products_list = Products.objects.all()
    paginator = Paginator(products_list, 12)

    page_number = request.GET.get('page')
    pages = paginator.page(page_number)
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'pages': pages,
    }
    return render(request, context)


def index(request):
    context = {
        'products': products,
        'products_vegetables': products_vegetables[:9],
        'products_vegetables_for_page': products_vegetables[:4],
        'products_fruits': products_fruits,
        'products_fruits_for_page': products_fruits[:4],
        'products_meat': products_meat,
        'products_category': products_all_category,
        'products_meat_count': products_meat_count,
        'products_fruits_count': products_fruits_count,
        'products_vegetables_count': products_vegetables_count,
    }
    return render(request, 'store/index.html', context)


def shop(request, category_id=None):
    products_list = Products.objects.filter(category_id=category_id) if category_id else Products.objects.all()
    paginator = Paginator(products_list, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products_list': products_list,
        'page_obj': page_obj,
        'products_meat_count': products_meat_count,
        'products_fruits_count': products_fruits_count,
        'products_vegetables_count': products_vegetables_count,
    }
    return render(request, 'store/shop.html', context)


def contact(request):
    return render(request, 'store/contact-us.html')


def cart(request):
    return render(request, 'store/cart.html')


def error(request):
    return render(request, 'store/404.html')


def checkout(request):
    return render(request, 'store/checkout.html')


def blog(request):
    return render(request, 'store/blog.html')


def blog_single(request):
    return render(request, 'store/blog-single.html')