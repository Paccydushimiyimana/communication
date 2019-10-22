from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser,Category


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    username = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Inform a valid email address.')
    phone = forms.CharField(max_length=10, help_text='Inform a valid phone.')

    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name','username','email','phone')

class MyUserChangeForm(UserChangeForm):

    class Meta:
        model = MyUser
        fields =('username','email')

    