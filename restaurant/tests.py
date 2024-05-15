from rest_framework import status
from rest_framework.test import APITestCase
from restaurant.models import OrderItem

class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url='http://127.0.0.1:8000/order-item/'
        data = {
        "quantity": 2,
        "guest": 1,
        "menu": 1
    },
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(OrderItem.objects.count(), 1)
        self.assertEqual(OrderItem.objects.get().menu,1)



