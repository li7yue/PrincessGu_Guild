'''
here we define class we need to use
classes are imported in admin, in order to show in dashboard
'''
# remember to update everything we modify models.py
# but different from settings, we need to makemigration first, then migrate

from django.db import models
from django.contrib.auth.models import User

class ToDoList(models.Model):
    '''
    A list, inherits from models.Model
    users linked with todolist using ForeignKey
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Item(models.Model):
    '''
    This is a class: An item, inherits from model.Model
    This class has the following Attributes(of an Item)
    '''
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    # ForeignKey links Item to ToDoList(Create a Union)
    text = models.CharField(max_length=200)
    complete = models.BooleanField()
    def __str__(self):
        return self.text
