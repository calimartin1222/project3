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
    items = list(menu_item.objects.values_list('item', flat=True).distinct())

    sizes = list(menu_item.objects.values_list('size', flat=True).distinct())

    pizzaTypes = list(menu_item.objects.values_list('type', flat=True).filter(item__in=['Pizza']).distinct())

    subTypes = list(menu_item.objects.values_list('type', flat=True).filter(item__in=['Sub']).distinct())

    pastaTypes = list(menu_item.objects.values_list('type', flat=True).filter(item__in=['Pasta']).distinct())

    saladTypes = list(menu_item.objects.values_list('type', flat=True).filter(item__in=['Salad']).distinct())

    platterTypes = list(menu_item.objects.values_list('type', flat=True).filter(item__in=['Dinner Platter']).distinct())

    subExtras = list(topping.objects.values_list('type', flat=True).filter(item__in=['Sub']).distinct())

    sizes.remove("N/A")

    toppings = topping.objects.all()

    return render(request, "orders/order.html", {'items' : items, 'toppings' : toppings,
    'sizes': sizes, 'pizzaTypes': pizzaTypes,  'subTypes': subTypes, 'pastaTypes': pastaTypes,
    'saladTypes': saladTypes, 'platterTypes': platterTypes, 'subExtras' : subExtras})

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