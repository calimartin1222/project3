from django.contrib import admin

# Register your models here.
from .models import menu_item, topping, item, size

admin.site.register(menu_item)
admin.site.register(topping)
admin.site.register(item)
admin.site.register(size)