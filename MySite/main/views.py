'''This file contains all views(pages)'''
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
# import class from models, if we want to pass them to html files as variables

def index(response, list_id):# this def accept addition attribute " an int", came from urls.py
    '''
    code for this view(page): to be updated
    '''
    var_list = ToDoList.objects.get(id=list_id)
    # if the list selected (selected by id) is in the reposne.user's todolist
    # it mean this list belongs to the user
    # else redirect to home page
    if var_list in response.user.todolist.all():
        if response.method == "POST":
            # the name attribute of buttons from list.html determine the if loop
            if response.POST.get("save"):
                # this was when we modified the attribute (complete) of items
                for item in var_list.item_set.all():
                    # on one hand, we take item from ToDoList(id=list_id)
                    # on the other hand, we check if item is being "clicked"
                    # (attribute has been modified)
                    if response.POST.get("c"+str(item.id)) == "clicked":
                        # if so, we modify the ToDoList instance
                        item.complete = True
                    else:
                        # if so, we modify the ToDoList instance
                        item.complete = False
                    item.save()# and remember to save it

            elif response.POST.get("newItem"):
                new_text = response.POST.get("preteam")# this is the name we input for new item
                new_dmg = response.POST.get("predmg")# this is the name we input for dmg
                new_time = response.POST.get("pretime")# this is the name we input for time
                if len(new_text) > 0 and len(new_dmg) > 0 and len(new_time) > 0:# add some naming rules
                    # the instance of ToDoList inherit django's models.Model class
                    # which has the create function
                    var_list.item_set.create(text=new_text, dmg=new_dmg, time=new_time, complete=False)
                else:
                    print("invalid")

            elif response.POST.get("duplicateItem"):
                new_text = response.POST.get("lastteam")# duplicate item
                new_dmg = response.POST.get("lastdmg")# duplicate dmg
                new_time = response.POST.get("lasttime")# duplicate time
                var_list.item_set.create(text=new_text, dmg=new_dmg, time=new_time, complete=False)

        return render(response, "main/list.html", {"var_list":var_list})
        # render passes response and variable(var_list) to the templates/main/list.html
    return render(response, "main/home.html", {})
    # unauth user will be rendered to home page

def home(response):
    '''
    code for this view(page): to be updated
    '''
    return render(response, "main/home.html", {})
    # render passes response to the templates/main/home.html

def create(response):
    '''
    this def create a instance(from class CreateNewList) and render it to create.html
    Check if we are receiving a POST request which would mean that the form has been submitted.
    If so, we will create a new form and fill it with the data we received from the request.
    Check if the form is valid, if so, we will create and save a new to do list object.
    Lastly we will redirect to the to do list we just created.
    '''
    if response.method == "POST":
        # CreateNewList is a class which inherits django's form.Forms
        # if str(response.user) != "AnonymousUser":# "If logged in" filter
        # Temp abandoned, because we want block everyone but Admin to create
        if str(response.user) == "Admin":# "Admin" filter
            form = CreateNewList(response.POST)
            if form.is_valid():# check if form is valid
                form_name = form.cleaned_data["name"]
                tdlist = ToDoList(name=form_name)
                tdlist.save()
                # after we login, the response has a user attribute
                # whenever we create a new list, it will be added to the current logged in user
                response.user.todolist.add(tdlist)
            return HttpResponseRedirect("/%i" % tdlist.id)
        else:
            return HttpResponseRedirect("/login")
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})

def view(response):
    '''
    if user is not anonymousUser,
    function let users to claim items by modifying item's owner attribute
    '''
    if str(response.user) != "AnonymousUser":
        all_list = ToDoList.objects.all()
        if response.method == "POST":
            item = Item.objects.get(id=response.POST.get('claim'))
            item.owner = str(response.user)
            item.save()
        return render(response, "main/view.html", {"all_list": all_list})
    return render(response, "main/view.html")

def knight(response):
    '''
    this function renders the knight page
    '''
    if str(response.user) != "AnonymousUser":
        all_list = ToDoList.objects.all()
        if response.method == "POST":
            item = Item.objects.get(id=response.POST.get('reportItem'))
            if (not item.complete) and (response.POST.get('actualdmg') != ''):
                item.complete = True
                item.actualDmg = response.POST.get('actualdmg')
                item.save()
        return render(response, "main/knight.html", {"all_list": all_list})
    return render(response, "main/view.html")
