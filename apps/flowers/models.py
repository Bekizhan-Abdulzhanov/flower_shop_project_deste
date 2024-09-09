from django.db import models
from apps.categories.models import Category
from django.contrib.auth import get_user_model
import os

User = get_user_model()


class Flower (models.Model):
    tag = models.ManyToManyField(
        Category,
        related_name='flower',
        verbose_name='Категории',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='product',
        verbose_name='пользователь',
    )
    title = models.CharField(
        max_length=150,
        verbose_name='Название',
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name='Цена',
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name='Дата',
    )

    def __str__(self):
        return self.title 
    

    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы'


class FlowerImage(models.Model):
    image = models.ImageField(
        upload_to='flower/',
    )
    flower = models.ForeignKey(
        Flower,
        on_delete=models.CASCADE,
        related_name='prog_img',
        verbose_name='фотографии',
    )

    def delete(self, using=None, keep_parents = False):
        os.remove(self.image.path)
        super().delete(using=None, keep_parents=False)

    
    def __str__(self):
        return self.image.path
    
    class Meta:
        verbose_name = 'Изображение Цветка'
        verbose_name_plural = 'Изображение Цветов'

        