'''
this file modifies the default sign up page
adding custom fields:
1. define them as class variables
2. add them into the field list
'''

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    '''
    A modified RegisterForm(class) inherit django's usercreationform
    new class variables can be created and added to the fields
    '''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
