from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    class GenderChoice(models.TextChoices):
        male = "male", "парень",
        female = "female", "девушка",

    photo = models.ImageField(
        upload_to='user/',
        verbose_name='картинка',
    )
    phone_number = PhoneNumberField(
        region='KG',
        verbose_name='Номер телефона',
    )
    gender = models.CharField(
        max_length=6,
        choices=GenderChoice.choices,
        verbose_name='пол',
        blank=True,
        null=True
    )
    age = models.PositiveIntegerField(
        verbose_name='Возраст',
        null=True,
    )
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'



