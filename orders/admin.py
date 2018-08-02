from django.contrib import admin

# Register your models here.
from .models import menu_item, topping, Order

admin.site.register(menu_item)
admin.site.register(topping)
admin.site.register(Order)