from django.conf import settings
from django.db import models


class ProductsCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(
        max_length=128,
    )
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to="products_images")
    category = models.ForeignKey(
        to=ProductsCategory, on_delete=models.PROTECT, null=True, blank=True
    )

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wished_item = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    yes_no = models.BooleanField(default=1)
    total_product = models.IntegerField()

    def __str__(self):
        return self.wished_item.name
