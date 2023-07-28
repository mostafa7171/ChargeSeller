from rest_framework import serializers
from seller.models import Seller, CreditIncreaseTransaction, CreditDecreaseTransaction, ChargeSaleTransaction


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


class CreditIncreaseTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditIncreaseTransaction
        fields = '__all__'


class CreditDecreaseTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditDecreaseTransaction
        fields = '__all__'


class ChargeSaleTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargeSaleTransaction
        fields = '__all__'
