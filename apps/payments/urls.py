from django.urls import path,include

from rest_framework.routers import DefaultRouter

from apps.payments import views

router = DefaultRouter()
router.register('payments',views.PaymentViewSet,basename='payments')

urlpatterns = [
    path('',include(router.urls)),
]