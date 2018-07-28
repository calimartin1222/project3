from django.contrib import admin

# Register your models here.
from .models import subType, pastaType, saladType, pizzaType, topping, platterType
# Pizza, Sub, Pasta, Salad, Platter,
#Register your models here.
# admin.site.register(Pizza)
# admin.site.register(Sub)
# admin.site.register(Pasta)
# admin.site.register(Salad)
# admin.site.register(Platter)

admin.site.register(subType)
admin.site.register(pastaType)
admin.site.register(saladType)
admin.site.register(platterType)
admin.site.register(topping)
admin.site.register(pizzaType)