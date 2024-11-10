from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, Select, FileInput, EmailInput, ModelForm

from product.models import Product, Category
from user.models import UserProfile


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

CITY = [    ('Istanbul', 'Istanbul'),
    ('Ankara', 'Ankara'),
    ('Izmir', 'Izmir'),]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address', 'city', 'state', 'image']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address', 'city', 'state', 'image']
        widgets = {
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'phone'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'address'}),
            'city': Select(attrs={'class': 'input', 'placeholder': 'city'}, choices=CITY),
            'state': TextInput(attrs={'class': 'input', 'placeholder': 'country'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image', }),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'last_name'}),
        }

# class MultiForm(UserUpdateForm,UserProfileForm):
#     class Meta:
#         model = User, user_profile
#         fields = ('username', 'email', 'first_name', 'last_name','phone_number', 'address', 'city', 'state', 'image')

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'title', 'keywords', 'description', 'image',
                  'price', 'detail']
        widgets = {
            'category': Select(attrs={'class': 'input', 'placeholder': 'Category'},
                               choices=Category.objects.all()),
            'title': TextInput(attrs={'class': 'input', 'placeholder': 'Title'}),
            'keywords': TextInput(attrs={'class': 'input', 'placeholder': 'Keywords'}),
            'description': TextInput(attrs={'class': 'input', 'placeholder': 'Description'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'Image', }),
            'price': TextInput(attrs={'class': 'input', 'placeholder': 'Price'}),
            'detail': CKEditorUploadingWidget(),
        }
