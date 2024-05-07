from django.contrib import admin

from .models import Dish, Beverage, Order, OrderedItem

admin.site.register(Dish)
admin.site.register(Beverage)
admin.site.register(Order)
admin.site.register(OrderedItem)
