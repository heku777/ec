from django.db import models
from django.utils import timezone

from shop.models import ShopItem

from django.conf import settings

User = settings.AUTH_USER_MODEL


class Cart(models.Model):
    class Meta:
        verbose_name = 'カート'
        verbose_name_plural = 'カート'

    user = models.OneToOneField(
        User,
        verbose_name='ユーザー',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        verbose_name='カート作成時間',
        default=timezone.now,
    )

    def __str__(self):
        return str(self.user)


class CartItem(models.Model):
    class Meta:
        verbose_name = 'カートアイテム'
        verbose_name_plural = 'カートアイテム'

    cart_user = models.ForeignKey(
        Cart,
        verbose_name='カートユーザー',
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        ShopItem,
        verbose_name='カートアイテム',
        on_delete=models.CASCADE,
    )
    product_number = models.IntegerField(
        verbose_name='購入数',
    )

    def price_tax(self):
        return '{:.0f}'.format(
            (int(self.product.price) * 1.08) * int(self.product_number))

    def __str__(self):
        return str(self.product)
