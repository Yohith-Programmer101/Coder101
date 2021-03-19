from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.views.generic.base import RedirectView
from .models import *
import requests
import bs4
from .forms import *

favicon = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def author(request):
    return render(request, "author.html")


def projects(request, id):
    model = Projects
    print(id)
    try:
        obj = Projects.objects.get(pk=id)
    except:
        return render(request, "project_not_found.html")
    if obj.is_site == True:
        return HttpResponseRedirect(obj.blob)
    else:
        site = requests.get(obj.blob)
        return HttpResponse(site)


def login(request):
    context = {}
    context["form"] = Login()
    return render(request, "Login/login.html", context)


def loggedin(request):
    context = {}
    user_name = request.POST["user_name"]
    password = request.POST["password"]
    if (user_name == "coder101") and (password == "coder101password"):
        context["title"] = "Welcome !"
        context["body"] = "You have logged in successfully !"
        return render(request, "Login/logged_in.html", context)
    else:
        context["form"] = Login()
        context["message"] = "Wrong Password Or User Name"
        return render(request, "Login/login.html", context)
