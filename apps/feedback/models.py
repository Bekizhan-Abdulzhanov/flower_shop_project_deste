from django.db import models
from django.contrib.auth import get_user_model
from apps.flowers.models import Flower 

User = get_user_model()

class FeedbackMain(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='feedbackmain',
        verbose_name='отзыв магазин',
    )
    text = models.TextField(
        verbose_name='Текст',
    )

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'отзыв магазину'
        verbose_name_plural = 'отзывы магазину'

        



class Feedback(models.Model):
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='feedback',
        verbose_name='отзыв',
    )
    flower = models.ForeignKey(
        Flower,
        on_delete=models.CASCADE,
        related_name='feedback',
        verbose_name='отзыв',
    )
    text = models.TextField(
        verbose_name='Текст',
    )

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'


class ReviewRating(models.Model):
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject