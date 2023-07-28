from django.db import models, transaction

from core.models import BaseModel
from rest_framework import status
from rest_framework.response import Response


class Seller(BaseModel):
    name = models.CharField(max_length=100)
    credit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_credit_increase = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_credit_decrease = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_charge_sale = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.credit < 0:
            self.credit = 0
        super().save(*args, **kwargs)


class CreditIncreaseTransaction(BaseModel):
    seller = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE,
        related_name="credit_increase_seller",
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    @transaction.atomic
    def save(self, *args, **kwargs):
        self.seller.total_credit_increase += self.amount
        self.seller.credit += self.amount
        self.seller.save()
        super().save(*args, **kwargs)


class CreditDecreaseTransaction(BaseModel):
    seller = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE,
        related_name="credit_decrease_seller",
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    @transaction.atomic
    def save(self, *args, **kwargs):
        if self.seller.credit >= self.amount:
            self.seller.total_credit_decrease += self.amount
            self.seller.credit -= self.amount
            self.seller.save()
            super().save(*args, **kwargs)
        else:
            raise ValueError("اعتبار ناکافی برای کاهش اعتبار.")


class ChargeSaleTransaction(BaseModel):
    seller = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE,
        related_name="charge_sale_seller",

    )
    mobile = models.CharField(max_length=11, default="")
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    @transaction.atomic
    def save(self, *args, **kwargs):
        if self.seller.credit >= self.amount:
            self.seller.total_charge_sale += self.amount
            self.seller.credit -= self.amount
            self.seller.save()
            super().save(*args, **kwargs)
        else:
            raise ValueError("اعتبار ناکافی برای فروش شارژ.")
