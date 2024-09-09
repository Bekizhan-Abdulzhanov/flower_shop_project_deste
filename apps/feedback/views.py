from rest_framework import viewsets
from apps.feedback.models import Feedback,ReviewRating,FeedbackMain
from apps.feedback.serializers import FeedbackSerializer,ReviewRatingSerializer,FeedbackMainSerializer

class FeedbackMainViewSet(viewsets.ModelViewSet):
    queryset = FeedbackMain.objects.all()
    serializer_class = FeedbackMainSerializer

    def get_queryset(self):
        user = self.request.user
        return FeedbackMain.objects.filter(user = user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        user = self.request.user 
        return Feedback.objects.filter(user=user)
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

    

