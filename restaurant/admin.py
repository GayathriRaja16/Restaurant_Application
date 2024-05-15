from django.contrib import admin

from .models import Guest, OrderItem, Order, Menu

admin.site.register([Menu, OrderItem, Order, Guest])
