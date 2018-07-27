from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader

# Create your views here.

def index(request):
      return render(request, "orders/index.html")