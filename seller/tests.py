from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.db import models
from seller.models import Seller, ChargeSaleTransaction


class SellerTransactionTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create Seller 1
        self.seller1 = Seller.objects.create(name='Seller 1', credit=5500)
        # Create Seller 2
        self.seller2 = Seller.objects.create(name='Seller 2', credit=2750)

    def test_charge_sale_transactions(self):
        # Create 10 charge sale transactions for Seller 1
        for i in range(1, 11):
            amount = i * 100  # Charge amount: 100, 200, ..., 1000
            response = self.client.post(reverse('seller:charge-sale-transactions-list'),
                                        data={'seller': self.seller1.id, 'amount': amount}, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Create 10 charge sale transactions for Seller 2
        for i in range(1, 11):
            amount = i * 50  # Charge amount: 50, 100, ..., 500
            response = self.client.post(reverse('seller:charge-sale-transactions-list'),
                                        data={'seller': self.seller2.id, 'amount': amount}, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check the updated credit of Seller 1
        seller1 = Seller.objects.get(id=self.seller1.id)
        self.assertEqual(seller1.credit, 0)

        # Check the updated credit of Seller 2
        seller2 = Seller.objects.get(id=self.seller2.id)
        self.assertEqual(seller2.credit, 0)

