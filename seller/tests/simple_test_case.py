# from django.test import TestCase
# from rest_framework.reverse import reverse
# from rest_framework import status
# from rest_framework.test import APIClient
# from django.db import models
# from seller.models import Seller, ChargeSaleTransaction
#
#
# class SellerTransactionTests(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         # Create Seller 1
#         self.seller1 = Seller.objects.create(name='Seller 1', credit=5500)
#         # Create Seller 2
#         self.seller2 = Seller.objects.create(name='Seller 2', credit=2750)
#
#     def test_charge_sale_transactions(self):
#         # Create 10 charge sale transactions for Seller 1
#         for i in range(1, 11):
#             amount = i * 100  # Charge amount: 100, 200, ..., 1000
#             response = self.client.post(reverse('seller:charge-sale-transactions-list'),
#                                         data={'seller': self.seller1.id, 'amount': amount}, format='json')
#             self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#         # Create 10 charge sale transactions for Seller 2
#         for i in range(1, 11):
#             amount = i * 50  # Charge amount: 50, 100, ..., 500
#             response = self.client.post(reverse('seller:charge-sale-transactions-list'),
#                                         data={'seller': self.seller2.id, 'amount': amount}, format='json')
#             self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#         # Check the updated credit of Seller 1
#         seller1 = Seller.objects.get(id=self.seller1.id)
#         self.assertEqual(seller1.credit, 0)
#
#         # Check the updated credit of Seller 2
#         seller2 = Seller.objects.get(id=self.seller2.id)
#         self.assertEqual(seller2.credit, 0)
#
#         total_charge_sale_seller1 = ChargeSaleTransaction.objects.filter(seller=self.seller1).aggregate(
#             total=models.Sum('amount'))
#         self.assertEqual(total_charge_sale_seller1['total'], 5500)
#
#         # Check the total_charge_sale of Seller 2
#         total_charge_sale_seller2 = ChargeSaleTransaction.objects.filter(seller=self.seller2).aggregate(
#             total=models.Sum('amount'))
#         self.assertEqual(total_charge_sale_seller2['total'], 2750)
#
#


from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from seller.models import Seller, CreditIncreaseTransaction, ChargeSaleTransaction


class SellerTransactionTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create Seller 1
        self.seller1 = Seller.objects.create(name='Seller 1')

        # Create Seller 2
        self.seller2 = Seller.objects.create(name='Seller 2')

    def test_credit_increase_transactions_seller1(self):
        # Create 10 credit increase transactions for Seller 1
        for i in range(1, 11):
            amount = i * 100000  # Increase amount: 100000, 200000, ..., 1000000
            url = reverse('seller:credit-increase-transactions-list')
            response = self.client.post(url, data={'seller': self.seller1.id, 'amount': amount}, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check the updated credit of Seller 1
        seller1 = Seller.objects.get(id=self.seller1.id)
        self.assertEqual(seller1.credit, sum(i * 100000 for i in range(1, 11)))

        # Create 1000 charge sale transactions for Seller 1
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

    def test_credit_increase_transactions_seller2(self):
        # Create 10 credit increase transactions for Seller 2
        for i in range(1, 11):
            amount = i * 200000  # Increase amount: 200000, 400000, ..., 2000000
            url = reverse('seller:credit-increase-transactions-list')
            response = self.client.post(url, data={'seller': self.seller2.id, 'amount': amount}, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check the updated credit of Seller 2
        seller2 = Seller.objects.get(id=self.seller2.id)
        self.assertEqual(seller2.credit, sum(i * 200000 for i in range(1, 11)))

        # Create 1000 charge sale transactions for Seller 2
        amount = 11000  # Charge amount: 11000
        mobile = '09374894286'
        url = reverse('seller:charge-sale-transactions-list')
        for i in range(1, 1001):
            response = self.client.post(url, data={'seller': self.seller2.id, 'mobile': mobile, 'amount': amount},
                                        format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check the updated credit of Seller 2
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
