from rest_framework import serializers
from apps.feedback.models import Feedback,FeedbackMain
from apps.feedback.models import ReviewRating


class FeedbackMainSerializer(serializers.ModelSerializer):
    class Meta:

        model = FeedbackMain
        fields = ['id','text']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id','flower','text']


class ReviewRatingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ReviewRating
        fields = ['id', 'flower', 'user', 'subject', 'review', 'rating', 'ip', 'status', 'created_at', 'updated_at']


