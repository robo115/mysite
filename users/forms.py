from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
       'class': 'col-sm-4', 'placeholder': 'password'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'surname'}))
    address_line1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address line 1'}))
    address_line2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address line 2'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    area = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Area'}))
    phone_number = PhoneNumberField(region='GE',  widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control', 'placeholder': 'phone number'}))
    image = forms.ImageField(widget=forms.ImageField)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'address_line1', 'address_line2', 'email', 'area', 'phone_number', 'image')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'confirm-password'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')