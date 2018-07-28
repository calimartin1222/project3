from django.db import models

# Create your models here.
class Pizza(models.Model):
    customer = models.CharField(max_length=64)
    kind = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    toppings = models.CharField(max_length=64)
    special = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.customer} ordered a {self.size}, {self.kind} Pizza with {self.toppings} - {self.special}."

class Sub(models.Model):
    customer = models.CharField(max_length=64)
    kind = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    extras = models.CharField(max_length=64)
    extraCheese = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.customer} ordered a {self.size}, {self.kind} Sub with {self.extras} - {self.extraCheese}."

class Pasta(models.Model):
    customer = models.CharField(max_length=64)
    kind = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.customer} ordered a {self.kind} pasta."

class Salad(models.Model):
    customer = models.CharField(max_length=64)
    kind = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.customer} ordered a {self.kind} salad."

class Platter(models.Model):
    customer = models.CharField(max_length=64)
    kind = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.customer} ordered a {self.kind} Dinner Platter."
#___________________________________________________________________________________________________________________________________
class subType(models.Model):
    type = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    price = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return f"{self.type} - ${self.price}"

class pizzaType(models.Model):
    type = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    price = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return f"{self.type} - ${self.price}"

class saladType(models.Model):
    type = models.CharField(max_length=64)
    price = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return f"{self.type} - ${self.price}"

class pastaType(models.Model):
    type = models.CharField(max_length=64)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return f"{self.type} - ${self.price}"

class platterType(models.Model):
    type = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return f"{self.type} - ${self.price}"

class topping(models.Model):
    type = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.type}"
