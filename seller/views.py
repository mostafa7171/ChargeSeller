from django.db import transaction
from rest_framework import viewsets, status
from seller.models import Seller, CreditIncreaseTransaction, CreditDecreaseTransaction, ChargeSaleTransaction
from seller.serializers import SellerSerializer, CreditIncreaseTransactionSerializer, \
    CreditDecreaseTransactionSerializer, \
    ChargeSaleTransactionSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [AllowAny]


class CreditIncreaseTransactionViewSet(viewsets.ModelViewSet):
    queryset = CreditIncreaseTransaction.objects.all()
    serializer_class = CreditIncreaseTransactionSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            serializer = CreditIncreaseTransactionSerializer(data=request.data)
            if serializer.is_valid():
                with transaction.atomic():
                    serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ValueError:
            return Response({"result": "اعتبار ناکافی برای کاهش اعتبار"},
                            status=status.HTTP_400_BAD_REQUEST)


# class CreditDecreaseTransactionViewSet(viewsets.ModelViewSet):
#     queryset = CreditDecreaseTransaction.objects.all()
#     serializer_class = CreditDecreaseTransactionSerializer
#     permission_classes = [AllowAny]
#
#     def create(self, request, *args, **kwargs):
#         try:
#             serializer = CreditDecreaseTransactionSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         except ValueError:
#             return Response({"result": "اعتبار ناکافی برای کاهش اعتبار"},
#                             status=status.HTTP_400_BAD_REQUEST)


class CreditDecreaseTransactionViewSet(viewsets.ModelViewSet):
    queryset = CreditDecreaseTransaction.objects.all()
    serializer_class = CreditDecreaseTransactionSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            serializer = CreditDecreaseTransactionSerializer(data=request.data)
            if serializer.is_valid():
                with transaction.atomic():
                    serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ValueError:
            return Response({"result": "اعتبار ناکافی برای کاهش اعتبار"},
                            status=status.HTTP_400_BAD_REQUEST)


# class ChargeSaleTransactionViewSet(viewsets.ModelViewSet):
#     queryset = ChargeSaleTransaction.objects.all()
#     serializer_class = ChargeSaleTransactionSerializer
#     permission_classes = [AllowAny]
#
#     def create(self, request, *args, **kwargs):
#         try:
#             serializer = CreditDecreaseTransactionSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         except ValueError:
#             return Response({"result": "اعتبار ناکافی برای فروش شارژ."},
#                             status=status.HTTP_400_BAD_REQUEST)


class ChargeSaleTransactionViewSet(viewsets.ModelViewSet):
    queryset = ChargeSaleTransaction.objects.all()
    serializer_class = ChargeSaleTransactionSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            serializer = ChargeSaleTransactionSerializer(data=request.data)
            if serializer.is_valid():
                with transaction.atomic():
                    serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ValueError:
            return Response({"result": "اعتبار ناکافی برای فروش شارژ."},
                            status=status.HTTP_400_BAD_REQUEST)
