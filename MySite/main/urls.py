'''Urls links to views'''
from django.urls import path
from . import views

urlpatterns = [
    # A link contains: path, file, name;
    # this is linked from MySite.urls(the top of all links), and from here, direct to views
    #
    # /<int:id> directs to view.index, (passing id as an attribute)
    path("<int:list_id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    path("knight/", views.knight, name="knight"),
]
