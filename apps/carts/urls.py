from django.urls import path, include
from apps.carts import views

from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()

router.register("carts", views.CartViewSet)

cart_router = routers.NestedDefaultRouter(router, "carts", lookup="cart")
router.register("items", views.CartItemViewSet, basename="cart-items")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(cart_router.urls))
]