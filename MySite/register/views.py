'''
add a function inside the views.py file of our register app to render this page
'''
from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(response):
    '''
    if POST, register using the response data linked from MySite/urls and redirect to home page
    since this is a higher level page than list and create
    '''
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})
