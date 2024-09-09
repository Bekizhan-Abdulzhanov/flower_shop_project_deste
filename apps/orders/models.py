from django.db import models
from apps.flowers.models import Flower
from django.contrib.auth import get_user_model
from apps.carts.models import Cart, CartItem

User = get_user_model()

STATUS_ORDER_CHOICES = (
    ('SUBMITTED', 'Submitted'),
    ('PRODUCTION', 'In Production'),
    ('DELIVERING', 'Left to Deliver'),
    ('DELIVERED', 'Delivered'),
    ('CANCELLED', 'Cancelled'),
)

STATUS_CITY_CHOICES = (
    ('OSH', 'Ош'),
    ('KARA-SYY', 'Кара-Суу'),
    ('KURSHAB', 'Куршаб'),
)

class UserAddress(models.Model):
    user = models.ForeignKey(
        User,
        null=False,
        on_delete=models.CASCADE
    )
    city_status = models.CharField(
        max_length=25,
        choices=STATUS_CITY_CHOICES,
        default='Ош',
        blank=False,
        verbose_name='Город',
    )
    street = models.TextField(
        null=False,
        verbose_name='Улица',
    )
    home = models.TextField(
        verbose_name='Дом',
    )

    def __str__(self):
        return self.street
 
    class Meta:
        verbose_name = 'Aдрес'
        verbose_name_plural = 'Адреса'


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='заказ',
    )
    user_address = models.ForeignKey(
        UserAddress,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Адрес'
    )
    flower = models.ForeignKey(
        Flower,
        on_delete=models.CASCADE,
    )
    order_status = models.CharField(
        max_length=25,
        choices=STATUS_ORDER_CHOICES,
        default='Submitted',
        blank=False,
    )
    cart = models.OneToOneField(
        Cart,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='order',
        verbose_name='заказ',

    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.user.username
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.quantity} x {self.flower.title} in Order {self.order.id}"
