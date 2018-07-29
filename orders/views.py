from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, "orders/index.html")

def menu(request):
    return render(request, "orders/menu.html")

