from django.db import models


class ProductsCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=128,)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductsCategory, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name

