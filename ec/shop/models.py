from django.db import models
from django.db.models import Avg


class ShopItem(models.Model):
    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'

    name = models.CharField(
        verbose_name='商品名',
        max_length=50,
        blank=True,
        null=True,
    )

    thumbnail = models.ImageField(
        verbose_name='商品画像',
        upload_to='media/'
    )

    price = models.IntegerField(
        verbose_name='商品価格',
        null=True,
        blank=True

    )

    stock = models.IntegerField(
        verbose_name='在庫数'
    )

    description = models.TextField(
        verbose_name='商品説明',
    )

    created = models.DateTimeField(
        verbose_name='商品作成日',
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name='商品更新日',
        auto_now=True,
    )

    @property
    def avg_rating(self):
        return self.reviews.all().aggregate(avg_rating=Avg('rating'))[
                   'avg_rating'] or 0

    def __str__(self):
        return self.name



