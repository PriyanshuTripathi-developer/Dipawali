from django import forms
from .models import Wish
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class WishForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ['name', 'wish_text', 'image']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
