from rest_framework import viewsets
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAdminUser

from .models import Guest, OrderItem, Order, Menu
from .serializers import (
    GuestSerializer,
    OrderItemSerializer,
    OrderSerializer,
    MenuSerializer,
)



class GuestView(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    
    # For Authentication purpose 
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
    http_method_names = ["get", "post", "put", "delete", "patch"]


class MenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
    http_method_names = ["get", "post", "put", "delete", "patch"]


class OrderItemView(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
    http_method_names = ["get", "post", "put", "delete", "patch"]


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
    http_method_names = ["get", "post", "put", "delete", "patch"]

    # Calculate and update price and final price before creating a new order
    def perform_create(self, serializer):
        price, final_price = self.update_price(serializer.validated_data)
        serializer.validated_data["price"] = price
        serializer.validated_data["final_price"] = final_price
        serializer.save()

    # Calculate and update price and final price before updating an order
    def perform_update(self, serializer):
        price, final_price = self.update_price(serializer.validated_data)
        serializer.validated_data["price"] = price
        serializer.validated_data["final_price"] = final_price
        serializer.save()

    # Calculate total price and final price for the order based on order items
    def update_price(self, instance):
        order_items = instance.get("order_item")
        price = 0
        final_price = 0

        if order_items:
            for order_item in order_items:
                price += order_item.menu.price * order_item.quantity

                # Apply a tax rate of 18%
                tax = price * 0.18  
                final_price = price + tax
        return price, final_price
