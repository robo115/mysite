from django.urls import path
from store.views import shop, product

app_name = 'store'

urlpatterns = [
    path('', shop, name='shop'),
    path('product-detalis/', product, name='product')
    ]
