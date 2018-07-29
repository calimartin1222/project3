from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from orders.models import *

# Create your views here.

def index(request):
    return render(request, "orders/index.html")

def menu(request):
    return render(request, "orders/menu.html")

@login_required
def order(request):
    menuItems = menuItem.objects.all()
    pizzaTypes = pizzaType.objects.all()
    toppings = topping.objects.all()
    return render(request, "orders/order.html", {'pizzaTypes' : pizzaTypes, 'toppings' : toppings, 'menuItems' : menuItems})

def placeOrder(request):
    if request.method =='POST':
        if form.is_valid():
            form.save()
            return redirect('/account')