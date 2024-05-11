from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r"dish", views.DishViewSet, basename="dish")
router.register(r"beverage", views.BeverageViewSet, basename="beverage")

urlpatterns = router.urls