from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone_number = PhoneNumberField(unique=True, null=True, blank=True)
    address_line1 = models.CharField(max_length=128, blank=True, null=True)
    address_line2 = models.CharField(max_length=128, blank=True, null=True)
    area = models.CharField(max_length=128, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='users_images')

