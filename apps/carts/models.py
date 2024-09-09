from django.db import models
from django.contrib.auth import get_user_model

from apps.flowers.models import Flower 

User = get_user_model()

class Cart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='пользователь',
    )

    def __str__(self):
        return self.user.username
    
class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='cart_flower',
        verbose_name='корзина',
    )
    item = models.ForeignKey(
        Flower,
        on_delete=models.CASCADE,
        related_name='cart_flower',
        verbose_name='цветок',
    )
    quantity = models.PositiveIntegerField(
        default=1,
    )
    def __str__(self):
        return self.item.title
    
    