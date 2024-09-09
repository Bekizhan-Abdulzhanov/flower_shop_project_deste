from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.flowers import views 


router = DefaultRouter()
router.register('flowers',views.FlowerViewSet,basename = 'flower')


urlpatterns = [
    path('',include(router.urls)),
]