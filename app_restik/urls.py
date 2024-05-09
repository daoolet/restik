from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),

    path("dishes/", views.DishView.as_view(), name="dish_view"),
]