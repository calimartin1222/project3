from django.contrib import admin

# Register your models here.
from .models import menu_item, topping
# Pizza, Sub, Pasta, Salad, Platter,
#Register your models here.
# admin.site.register(Pizza)
# admin.site.register(Sub)
# admin.site.register(Pasta)
# admin.site.register(Salad)
# admin.site.register(Platter)

admin.site.register(menu_item)
admin.site.register(topping)