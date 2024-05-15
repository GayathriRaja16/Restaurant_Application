from rest_framework import serializers
from .models import Guest, OrderItem, Order, Menu


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
