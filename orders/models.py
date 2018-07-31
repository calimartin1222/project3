from django.db import models

#class order():


class menu_item(models.Model):
    type = models.CharField(max_length=64)
    item = models.CharField(max_length=64, default="Pizza")
    special = models.BooleanField(default=False)
    size = models.CharField(max_length=64, default="Small")
    toppings = models.IntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=4, default=0.00)

    def __str__(self):
        special_if=""
        if(self.special):
            special_if="Special"
            return f"{special_if} {self.size} {self.type} {self.item} - {self.price}"
        elif(self.toppings==0):
            return f"{self.size} {self.type} {self.item} - {self.price}"
        elif(self.toppings==1):
            return f"{special_if} {self.size} {self.type} {self.item} with {self.toppings} topping - {self.price}"
        else:
            special_if=""
            return f"{special_if} {self.size} {self.type} {self.item} with {self.toppings} toppings - {self.price}"

class topping(models.Model):
    item = models.CharField(max_length=64, default="Pizza")
    type = models.CharField(max_length=64)
    price = models.DecimalField(decimal_places=2, max_digits=4, default=0.00)
    def __str__(self):
        if self.price==0.00:
            return f"{self.item} - {self.type}"
        else:
            return f"{self.item} - {self.type} Extra {self.price}"

class item(models.Model):
    item = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.item}"

class size(models.Model):
    size = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.size}"