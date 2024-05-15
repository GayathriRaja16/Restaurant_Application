from django.db import models

# Choices for the type of food (veg or non-veg)
FOOD_CHOICES = [
    ("veg", "veg"),
    ("non-veg", "non-veg"),
]


class Guest(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(null=True, blank=True, default=None)
    phone_number = models.CharField(max_length=10, unique=True, default=None)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "guest"


class Menu(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField()
    type_of_food = models.CharField(choices=FOOD_CHOICES, max_length=10)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "menu"


class OrderItem(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.guest} | {self.menu} | {self.quantity}"

    class Meta:
        db_table = "order_item"

    # Update order when saving order-item
    def save(self, *args, **kwargs):
        super(OrderItem, self).save(*args, **kwargs)
        self.update_orders()

    # Calculate total and final price for the order
    def update_orders(self):
        try:
            for order in self.order_set.all():
                total_price = sum(
                    order_item.menu.price * order_item.quantity
                    for order_item in order.order_item.all()
                )
                # Apply GST 18%
                final_price = total_price + (total_price * 0.18)
                order.price = total_price
                order.final_price = final_price
                order.save()
        except:
            print("Error in method update order")



class Order(models.Model):
    order_item = models.ManyToManyField(OrderItem)
    price = models.FloatField(blank=True, default=0)
    final_price = models.FloatField(blank=True, default=0)

    def __str__(self) -> str:
        return f"{self.price} - {self.final_price}"

    class Meta:
        db_table = "order"
  
