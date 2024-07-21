from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class ReviewForm(forms.Form):
        customer_name = forms.CharField(max_length=100, required=True)
        profession_name = forms.CharField(max_length=100, required=True)
        review_text = forms.CharField(widget=forms.Textarea, required=True)

class RegisterForm(UserCreationForm):
        first_name = forms.CharField(max_length=100, required=True)
        last_name = forms.CharField(max_length=100, required=True)
        email = forms.EmailField(required=True)
        password1 = forms.CharField(label = "Password", widget=forms.PasswordInput)
        password2 =  forms.CharField(label = "Confirm your password", widget=forms.PasswordInput)

        class Meta:
                model = User
                fields = ["username", "first_name", "last_name", "email", "password1", "password2", ]

class UserEditForm(UserChangeForm):
        first_name = forms.CharField(label= "first_name", max_length=100, required=True)
        last_name = forms.CharField(label= "last_name", max_length=100, required=True)
        email = forms.EmailField(required=True)

        class Meta:
                model = User
                fields = ["username", "first_name", "last_name", "email"]


class AvatarForm(forms.Form):
        imagen = forms.ImageField(required=True)