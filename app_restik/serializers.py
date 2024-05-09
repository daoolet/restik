from rest_framework import serializers

from . import models


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dish
        fields = "__all__"


class BeverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Beverage
        fields = "__all__"