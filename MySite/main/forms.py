'''The Forms class using Django's forms'''
# https://docs.djangoproject.com/en/2.2/topics/forms/

from django import forms
import copy

class CreateNewList(forms.Form):
    '''Inherit from Django's forms.Form, and create attributes name and check'''
    name = forms.CharField(label="Name", max_length=200)
    required_dmg = forms.IntegerField()
    hp = forms.IntegerField()
    check = forms.BooleanField(required=False)
