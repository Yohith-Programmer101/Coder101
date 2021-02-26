from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from .models import *
import requests
import bs4


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def author(request):
    return render(request, "author.html")


def projects(request, id):
    model = Projects
    try:
        obj = Projects.objects.all(pk=id)
    except:
        return render(request, "project_not_found.html")
    if obj.is_site == True:
        return HttpResponseRedirect(obj.blob)
    else:
        site = requests.get(obj.blob)
        return HttpResponse(site)
