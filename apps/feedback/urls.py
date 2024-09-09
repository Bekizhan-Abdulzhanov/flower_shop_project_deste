from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.feedback import views

router = DefaultRouter()
router.register('feedbacks',views.FeedbackViewSet,basename='feedback'),
router.register('feedbackMain',views.FeedbackMainViewSet,basename='feedbackMain'),



urlpatterns = [
    path('',include(router.urls)),
]