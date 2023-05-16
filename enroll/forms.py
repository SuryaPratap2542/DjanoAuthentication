from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms

class SignUpForm(UserCreationForm):
    age = forms.IntegerField(label='Enter age')
    password2 = forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','age']
        labels = {'email':'your Email'}

class EditUserProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login']
        labels={'enail':'Your Email'}
