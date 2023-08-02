from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from seller.models import Seller


class SellerTransactionTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.seller1 = Seller.objects.create(name='Seller 1')

        self.seller2 = Seller.objects.create(name='Seller 2')

    def test_transactions_seller1(self):
        for i in range(1, 11):
            amount = i * 100000  # Increase amount: 100000, 200000, ..., 1000000
            url = reverse('seller:credit-increase-transactions-list')
            response = self.client.post(url, data={'seller': self.seller1.id, 'amount': amount}, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        seller1 = Seller.objects.get(id=self.seller1.id)
        self.assertEqual(seller1.credit, sum(i * 100000 for i in range(1, 11)))

        amount = 5500  # Charge amount: 5500
        mobile = '09169611977'
        url = reverse('seller:charge-sale-transactions-list')
        for i in range(1, 1001):
            response = self.client.post(url, data={'seller': self.seller1.id, 'mobile': mobile, 'amount': amount},
                                        format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check the updated credit of Seller 1
        seller1 = Seller.objects.get(id=self.seller1.id)
        self.assertEqual(seller1.credit + (amount * 1000), amount * 1000)

    def test_transactions_seller2(self):
        for i in range(1, 11):
            amount = i * 200000  # Increase amount: 200000, 400000, ..., 2000000
            url = reverse('seller:credit-increase-transactions-list')
            response = self.client.post(url, data={'seller': self.seller2.id, 'amount': amount}, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        seller2 = Seller.objects.get(id=self.seller2.id)
        self.assertEqual(seller2.credit, sum(i * 200000 for i in range(1, 11)))

        amount = 11000  # Charge amount: 11000
        mobile = '09374894286'
        url = reverse('seller:charge-sale-transactions-list')
        for i in range(1, 1001):
            response = self.client.post(url, data={'seller': self.seller2.id, 'mobile': mobile, 'amount': amount},
                                        format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        seller2 = Seller.objects.get(id=self.seller2.id)
        self.assertEqual(seller2.credit + (amount * 1000), amount * 1000)





    # def test_charge_sale_transactions_seller1(self):
    #     # Create 1000 charge sale transactions for Seller 1
    #     amount = 5500  # Charge amount: 5500
    #     mobile = '09169611977'
    #     url = reverse('seller:charge-sale-transactions-list')
    #     for i in range(1, 1001):
    #         response = self.client.post(url, data={'seller': self.seller1.id, 'mobile': mobile, 'amount': amount},
    #                                     format='json')
    #         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #
    #     # Check the updated credit of Seller 1
    #     seller1 = Seller.objects.get(id=self.seller1.id)
    #     print(seller1.credit)
    #     self.assertEqual(seller1.credit + (amount * 1000), amount * 1000)
    #
    # def test_charge_sale_transactions_seller2(self):
    #     # Create 1000 charge sale transactions for Seller 2
    #     amount = 11000  # Charge amount: 11000
    #     mobile = '09374894286'
    #     url = reverse('seller:charge-sale-transactions-list')
    #     for i in range(1, 1001):
    #         response = self.client.post(url, data={'seller': self.seller2.id, 'mobile': mobile, 'amount': amount},
    #                                     format='json')
    #         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #
    #     # Check the updated credit of Seller 2
    #     seller2 = Seller.objects.get(id=self.seller2.id)
    #     print(seller2.credit)
    #
    #     self.assertEqual(seller2.credit + (amount * 1000), amount * 1000)
