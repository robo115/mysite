from django.urls import path
from store.views import shop

app_name = 'store'

urlpatterns = [
    path('', shop, name='shop'),
    path('category/<int:category_id>', shop, name='category'),
    ]
