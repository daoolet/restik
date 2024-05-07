from django.db import models


class Dish(models.Model):
    STARTER = "SS"
    SALAD = "SD"
    SOUP = "SP"
    MAIN = "MN"
    SIDE = "SE"
    DESSERT = "DS"
    
    DISH_CATEGORY_CHOICES = {
        STARTER : "Starter",
        SALAD : "Salads",
        SOUP : "Soup",
        MAIN : "Main",
        SIDE : "Side",
        DESSERT : "Dessert",
    } 

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(
        max_length=2,
        choices=DISH_CATEGORY_CHOICES,
        default=None
    )


    class Meta:
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.name
    

class Beverage(models.Model):
    STIMULATING = "ST"
    REFRESHING = "RF"
    ALCOHOL = "AL"
    NOURISHING = "NR"
    
    BEVERAGE_CATEGORY_CHOICES = {
        STIMULATING : "Stimulating",
        REFRESHING : "Refreshing",
        ALCOHOL : "Alcohol",
        NOURISHING : "Nourishing",
    } 


    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.FloatField()
    category = models.CharField(
        max_length=2,
        choices=BEVERAGE_CATEGORY_CHOICES,
        default=None
    )


    class Meta:
        verbose_name = "Beverage"
        verbose_name_plural = "Beverages"

    def __str__(self):
        return self.name
    

class Order(models.Model):
    IN_PROCESS = "PR"
    DONE = "DN"
    CANCELLED = "CN"

    ORDER_STATUS_CHOICES = {
        IN_PROCESS : "In process",
        DONE : "Done",
        CANCELLED : "Cancelled",
    }


    # customer = 
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=2,
        choices=ORDER_STATUS_CHOICES,
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
    quantity = models.IntegerField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.dish.name} ({self.quantity})"