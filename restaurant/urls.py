from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GuestView, MenuView, OrderView, OrderItemView

router = DefaultRouter()

# Register viewsets with corresponding endpoints
router.register("menu", MenuView, basename="menu")
router.register("guest", GuestView, basename="guest")
router.register("order-item", OrderItemView, basename="order_item")
router.register("order", OrderView, basename="order")

# Include router-generated URLs
urlpatterns = [
    path("", include(router.urls)),
]
