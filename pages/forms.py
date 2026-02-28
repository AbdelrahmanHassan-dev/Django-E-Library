from django import forms
from books.models import Messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Contact_us(forms.ModelForm):
    class Meta:
        model= Messages
        fields = '__all__'

class Signup(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = {'username','password1','password2','email'}