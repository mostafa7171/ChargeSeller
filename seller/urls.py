from django.urls import path, include
from rest_framework.routers import DefaultRouter
from seller.views import SellerViewSet, CreditIncreaseTransactionViewSet, CreditDecreaseTransactionViewSet, \
    ChargeSaleTransactionViewSet

router = DefaultRouter()
router.register(r'sellers', SellerViewSet, basename='sellers')
router.register(r'credit-increase-transactions', CreditIncreaseTransactionViewSet,
                basename='credit-increase-transactions')
router.register(r'credit-decrease-transactions', CreditDecreaseTransactionViewSet,
                basename='credit-decrease-transactions')
router.register(r'charge-sale-transactions', ChargeSaleTransactionViewSet, basename='charge-sale-transactions')

app_name = "seller"
urlpatterns = [
    path('', include(router.urls)),
]