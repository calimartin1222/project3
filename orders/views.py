from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from orders.models import *
from django.forms.models import model_to_dict

# Create your views here.

def index(request):
    return render(request, "orders/index.html")

def menu(request):
    return render(request, "orders/menu.html")

@login_required
def order(request):
    menuItems = menu_item.objects.all()
    toppings = topping.objects.all()
    return render(request, "orders/order.html", {'menuItems' : menuItems, 'toppings' : toppings})

@login_required
def cart(request):
    if request.method == "POST":
        order = menu_item.objects.get(item = "Pizza", size = "Large")
        args = {
            'order' : order
        }
        return render(request, 'orders/cart.html', args)
    else:
        return render(request, 'orders/cart.html')