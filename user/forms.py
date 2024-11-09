from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=25, label="Username")
    email = forms.EmailField(max_length=100,label="Email")
    first_name = forms.CharField(max_length=25, label="First Name")
    last_name = forms.CharField(max_length=25, label="Last Name")

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','password1','password2')