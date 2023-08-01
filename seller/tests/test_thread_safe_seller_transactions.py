import pytest
from rest_framework import status
from rest_framework.test import APIClient
from seller.models import Seller
from django.urls import reverse
from django.db import transaction


@pytest.mark.django_db
def create_charge_sale_transactions(seller, amount, mobile):
    url = reverse('seller:charge-sale-transactions-list')
    for i in range(1000):
        data = {'seller': seller.id, 'mobile': mobile, 'amount': amount}
        response = APIClient().post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_credit_increase_transactions_seller1():
    seller1 = Seller.objects.create(name='Seller 1')

    for i in range(1, 11):
        amount = i * 100000
        url = reverse('seller:credit-increase-transactions-list')
        data = {'seller': seller1.id, 'amount': amount}
        response = APIClient().post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    seller1 = Seller.objects.get(id=seller1.id)
    assert seller1.credit == sum(i * 100000 for i in range(1, 11))

    amount = 5500
    mobile = '09169611977'
    with transaction.atomic():
        create_charge_sale_transactions(seller1, amount, mobile)

    seller1 = Seller.objects.get(id=seller1.id)
    assert seller1.credit + (amount * 1000) == amount * 1000


@pytest.mark.django_db
def test_credit_increase_transactions_seller2():
    seller2 = Seller.objects.create(name='Seller 2')

    for i in range(1, 11):
        amount = i * 200000
        url = reverse('seller:credit-increase-transactions-list')
        data = {'seller': seller2.id, 'amount': amount}
        response = APIClient().post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    seller2 = Seller.objects.get(id=seller2.id)
    assert seller2.credit == sum(i * 200000 for i in range(1, 11))

    amount = 11000
    mobile = '09374894286'
    with transaction.atomic():
        create_charge_sale_transactions(seller2, amount, mobile)

    seller2 = Seller.objects.get(id=seller2.id)
    assert seller2.credit + (amount * 1000) == amount * 1000



# import pytest
# from rest_framework import status
# from rest_framework.test import APIClient
# from seller.models import Seller
# from django.urls import reverse
# import threading
#
# charge_sale_lock = threading.Lock()
#
#
# @pytest.mark.django_db
# def create_charge_sale_transactions(seller, amount, mobile):
#     url = reverse('seller:charge-sale-transactions-list')
#     for i in range(1000):
#         data = {'seller': seller.id, 'mobile': mobile, 'amount': amount}
#         response = APIClient().post(url, data, format='json')
#         assert response.status_code == status.HTTP_201_CREATED
#
#
# @pytest.mark.django_db
# def test_credit_increase_transactions_seller1():
#     seller1 = Seller.objects.create(name='Seller 1')
#
#     for i in range(1, 11):
#         amount = i * 100000
#         url = reverse('seller:credit-increase-transactions-list')
#         data = {'seller': seller1.id, 'amount': amount}
#         response = APIClient().post(url, data, format='json')
#         assert response.status_code == status.HTTP_201_CREATED
#
#     seller1 = Seller.objects.get(id=seller1.id)
#     assert seller1.credit == sum(i * 100000 for i in range(1, 11))
#
#     amount = 5500
#     mobile = '09169611977'
#     with charge_sale_lock:
#         create_charge_sale_transactions(seller1, amount, mobile)
#
#     seller1 = Seller.objects.get(id=seller1.id)
#     assert seller1.credit + (amount * 1000) == amount * 1000
#
#
# @pytest.mark.django_db
# def test_credit_increase_transactions_seller2():
#     seller2 = Seller.objects.create(name='Seller 2')
#
#     for i in range(1, 11):
#         amount = i * 200000
#         url = reverse('seller:credit-increase-transactions-list')
#         data = {'seller': seller2.id, 'amount': amount}
#         response = APIClient().post(url, data, format='json')
#         assert response.status_code == status.HTTP_201_CREATED
#
#     seller2 = Seller.objects.get(id=seller2.id)
#     assert seller2.credit == sum(i * 200000 for i in range(1, 11))
#
#     amount = 11000
#     mobile = '09374894286'
#     with charge_sale_lock:
#         create_charge_sale_transactions(seller2, amount, mobile)
#
#     seller2 = Seller.objects.get(id=seller2.id)
#     assert seller2.credit + (amount * 1000) == amount * 1000
