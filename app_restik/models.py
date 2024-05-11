from django.db import models
from django.core.validators import MinValueValidator

from . import utils


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    category = models.CharField(
        max_length=20,
        choices=utils.DISH_CATEGORY_CHOICES,
        default=None
    )

    class Meta:
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.name
    

class Beverage(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.FloatField()
    category = models.CharField(
        max_length=20,
        choices=utils.BEVERAGE_CATEGORY_CHOICES,
        default=None
    )

    class Meta:
        verbose_name = "Beverage"
        verbose_name_plural = "Beverages"

    def __str__(self):
        return self.name
    

class Order(models.Model):
    # customer = 
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=utils.ORDER_STATUS_CHOICES,
        default=None
    )

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self) -> str:
        return f"Order {self.id}"


class OrderedItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.dish.name} ({self.quantity})"