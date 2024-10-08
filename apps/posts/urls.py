from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.posts import views 

router = DefaultRouter()
router.register('posts',views.PostViewSet,basename='post')

urlpatterns = [
    path('',include(router.urls))
]