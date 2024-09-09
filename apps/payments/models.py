from django.db import models
from django.contrib.auth import get_user_model
from apps.orders.models import Order

User = get_user_model()

PAYMENT_STATUS_CHOICES = (
    ('PENDING', 'В ожидании'),
    ('COMPLETED', 'Завершено'),
    ('FAILED', 'Отклонено'),
    ('REFUNDED', 'Возращено'),
)


PAYMENT_METHOD_CHOICES = (
    ('CREDIT_CARD', 'Кредитной карточкой'),
    ('PAYPAL', 'PayPal'),
    ('BANK_TRANSFER', 'Банковский перевод'),
    ('Mbank','Мобильный перевод'),
)

class Payment(models.Model):
    user = models.ForeignKey(
        User,on_delete=models.CASCADE,
        related_name='payments',
        verbose_name='оплата',
    )
    order=models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name='payment',
        verbose_name='оплата',)
    amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
    )
    status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default='В ожидании',
    )
    method = models.CharField(
        max_length=30,
        choices=PAYMENT_METHOD_CHOICES,
        default='Mbank',
    )
    created_at=models.DateTimeField(
            auto_now_add = True,
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'

    def __str__(self):
        return f"Payment {self.id} for Order {self.order.id}"