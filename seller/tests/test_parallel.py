import pytest
from rest_framework import status
from rest_framework.test import APIClient
from seller.models import Seller
from django.urls import reverse


@pytest.mark.django_db
def test_parallel_transactions_seller1():
    seller1 = Seller.objects.create(name='Seller 1')

    for i in range(1, 11):
        amount = i * 100000  # Increase amount: 100000, 200000, ..., 1000000
        url = reverse('seller:credit-increase-transactions-list')
        data = {'seller': seller1.id, 'amount': amount}
        response = APIClient().post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    seller1 = Seller.objects.get(id=seller1.id)
    assert seller1.credit == sum(i * 100000 for i in range(1, 11))

    amount = 5500  # Charge amount: 5500
    mobile = '09169611977'
    url = reverse('seller:charge-sale-transactions-list')
    for i in range(1, 1001):
        data = {'seller': seller1.id, 'mobile': mobile, 'amount': amount}
        response = APIClient().post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    seller1 = Seller.objects.get(id=seller1.id)
    assert seller1.credit + (amount * 1000) == amount * 1000


@pytest.mark.django_db
def test_parallel_transactions_seller2():
    seller2 = Seller.objects.create(name='Seller 2')

    for i in range(1, 11):
        amount = i * 200000  # Increase amount: 200000, 400000, ..., 2000000
        url = reverse('seller:credit-increase-transactions-list')
        data = {'seller': seller2.id, 'amount': amount}
        response = APIClient().post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    seller2 = Seller.objects.get(id=seller2.id)
    assert seller2.credit == sum(i * 200000 for i in range(1, 11))

    amount = 11000  # Charge amount: 11000
    mobile = '09374894286'
    url = reverse('seller:charge-sale-transactions-list')
    for i in range(1, 1001):
        data = {'seller': seller2.id, 'mobile': mobile, 'amount': amount}
        response = APIClient().post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    seller2 = Seller.objects.get(id=seller2.id)
    assert seller2.credit + (amount * 1000) == amount * 1000








#
# # @pytest.mark.django_db
# # def test_charge_sale_transactions_seller1():
# #     # Your test logic for charge sale transactions for Seller 1
# #     # Create Seller 1
# #     seller1 = Seller.objects.create(name='Seller 1')
# #
# #     # Create 1000 charge sale transactions for Seller 1
# #     amount = 5500  # Charge amount: 5500
# #     mobile = '09169611977'
# #     url = reverse('seller:charge-sale-transactions-list')
# #     for i in range(1, 1001):
# #         data = {'seller': seller1.id, 'mobile': mobile, 'amount': amount}
# #         response = APIClient().post(url, data, format='json')
# #         assert response.status_code == status.HTTP_201_CREATED
# #
# #     # Check the updated credit of Seller 1
# #     seller1 = Seller.objects.get(id=seller1.id)
# #     assert seller1.credit == amount * 1000
# #
# #
# # @pytest.mark.django_db
# # def test_charge_sale_transactions_seller2():
# #     # Your test logic for charge sale transactions for Seller 2
# #     seller2 = Seller.objects.create(name='Seller 2')
# #
# #     # Create 1000 charge sale transactions for Seller 2
# #     amount = 11000  # Charge amount: 11000
# #     mobile = '09374894286'
# #     url = reverse('seller:charge-sale-transactions-list')
# #     for i in range(1, 1001):
# #         data = {'seller': seller2.id, 'mobile': mobile, 'amount': amount}
# #         response = APIClient().post(url, data, format='json')
# #         assert response.status_code == status.HTTP_201_CREATED
# #
# #     # Check the updated credit of Seller 2
# #     seller2 = Seller.objects.get(id=seller2.id)
# #     assert seller2.credit == amount * 1000
