from django.shortcuts import render, HttpResponse, get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from drf_spectacular.utils import extend_schema

from .models import Dish, Beverage
from .serializers import DishSerializer, BeverageSerializer


def home(request):
    return HttpResponse("Hello World")


class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class BeverageViewSet(ModelViewSet):
    queryset = Beverage.objects.all()
    serializer_class = BeverageSerializer