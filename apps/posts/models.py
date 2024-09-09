from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        )

    name = models.CharField(
        max_length=150,
        verbose_name='Название',
    )
    text = models.TextField(
        verbose_name='Описание',
    )

    def __str__(self):
        return self.name
    
class Meta: 
    verbose_name = 'Пост'
    verbose_name_plural = 'Посты'