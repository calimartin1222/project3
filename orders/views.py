from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from orders.models import *
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from decimal import *

# Create your views here

def index(request):
    return render(request, "orders/index.html")

def menu(request):
    return render(request, "orders/menu.html")

@login_required
def order(request):
    #get attributes of menu items from database
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

    #sends the menu item attributes to the order page to print them out in forms where the user can pick what they want

    return render(request, "orders/order.html", {'items' : items, 'toppings' : toppings,
    'sizes': sizes, 'pizzaTypes': pizzaTypes,  'subTypes': subTypes, 'pastaTypes': pastaTypes,
    'saladTypes': saladTypes, 'platterTypes': platterTypes, 'subExtras' : subExtras,
    'user': request.user})

@login_required
@csrf_exempt
def cart(request):
    #gets name of current user that made the request
    user = request.user
    #if the request method was post i.e. they submitted info via form to this page
    if request.method == "POST":
        #gets all the data from the form
        user = str(request.user).lower()
        item = str(request.POST.get("item"))
        size = str(request.POST.get("size"))
        type = str(request.POST.get("type"))
        toppings = int(request.POST.get("toppings"))
        extras = int(request.POST.get("extras"))
        special = bool(request.POST.get("is_special"))
        #sets up what to do because each item has different characteristics
        if(item == "Pizza"):
            item_get = menu_item.objects.get(item = item, size = size, type = type, toppings = toppings, special = special)
        if(item == "Sub"):
            item_get = menu_item.objects.get(item = item, size = size, type = type, toppings = extras)
        if(item == "Pasta"):
            item_get = menu_item.objects.get(item = item, type = type)
        if(item == "Salad"):
            item_get = menu_item.objects.get(item = item, size = size, type = type)
        if(item == "Dinner Platter"):
            item_get = menu_item.objects.get(item = item, size = size, type = type)
        #gets the id of the menu item
        item_id = item_get.id
        #creates new Order model object with menu item id and user name
        o = Order.objects.create(name=user, item_id=item_id)
        o.save()
        return render(request, 'orders/cart.html')
    #if it is accessed via a get request
    else:
        pending=''
        total_price = Decimal(0.00)
        order_list = []
        matched_orders = []
        objs = []

        orders = list(Order.objects.values_list('item_id', flat=True).filter(name__in=[user]))

        for x in orders:

            matched_orders = menu_item.objects.filter(id=x)

            objs = Order.objects.filter(item_id=x)

            for obj in objs:

                for matched_order in matched_orders:
                    order_list.append(matched_order)
                    total_price += matched_order.price

                if(obj.completed == True):
                    pending = "Order Completed!"
                else:
                    pending = "Order Pending..."

                order_list.append(pending)
        args = {
            'orders': order_list,
            'total_price': total_price
        }

        return render(request, 'orders/cart.html', args)

def directions(request):
    return render(request, 'account/directions.html')

def hours(request):
    return render(request, 'account/hours.html')

def sicilianVSreg(request):
    return render(request, 'account/hours.html')

def contact(request):
    return render(request, 'account/contact.html')