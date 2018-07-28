from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader

# Create your views here.

def index(request):
      return render(request, "orders/index.html")

def order(request):
    subTypes = subTypes.objects.all()
    subTypeList = subscription_id.values()
    return render(request, "orders/order.html", subTypeList = subTypeList)

def placeorder(request):
    customer = request.POST["passenger"]