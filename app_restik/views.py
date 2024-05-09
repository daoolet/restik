from django.shortcuts import render, HttpResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema

from .models import Dish, Beverage
from .serializers import DishSerializer, BeverageSerializer


def home(request):
    return HttpResponse("Hello World")


class DishView(APIView):
    serializer_class = DishSerializer

    def get(self, request):
        all_dishes = Dish.objects.all()
        serializer = DishSerializer(all_dishes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # @extend_schema(request=DishSerializer)
    def post(self, request):
        serializer = DishSerializer(data=request.data)

        if serializer.is_valid():
            dish_name = serializer.validated_data["name"]

            if Dish.objects.filter(name=dish_name).exists():
                return Response({"detail": "Already exists"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                dish = serializer.save()
                return Response({
                    "detail": "Successful",
                    "dish_id": dish.id
                }, status=status.HTTP_200_OK)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)