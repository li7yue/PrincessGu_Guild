'''
This page is meant to show us (the admin) information about our site and database. 
Modify this file to add database(what to show) to this dashboard
'''
from django.contrib import admin
from .models import ToDoList, Item# import class from models to show them in dashboard

# Database
admin.site.register(ToDoList)
admin.site.register(Item)
