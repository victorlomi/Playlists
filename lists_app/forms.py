from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Enter a valid email address.")
    profile_photo = forms.ImageField(label="Select a profile image")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'profile_photo')
