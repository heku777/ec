from django.db import models
from django.conf import settings
from shop.models import ShopItem

User = settings.AUTH_USER_MODEL


class Review(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='ユーザ',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        ShopItem,
        related_name='reviews',
        verbose_name='商品',
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(
        verbose_name='評価',
        default=0
    )
    title = models.CharField(
        verbose_name='タイトル',
        null=False,
        blank=False,
        max_length=255
    )
    comment = models.TextField(
        verbose_name='コメント',
        blank=True,
        null=True
    )
