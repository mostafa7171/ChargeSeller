from django.contrib import admin
from seller.models import Seller, CreditIncreaseTransaction, CreditDecreaseTransaction, ChargeSaleTransaction

admin.site.register(Seller)
admin.site.register(CreditIncreaseTransaction)
admin.site.register(CreditDecreaseTransaction)
admin.site.register(ChargeSaleTransaction)
