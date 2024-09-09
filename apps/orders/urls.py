from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.orders.views import UserAddressViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'user_addresses', UserAddressViewSet, basename='useraddress')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path
from .views import OrderViewSet
