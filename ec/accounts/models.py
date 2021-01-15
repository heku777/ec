from django.contrib.auth.models import AbstractUser
from django.db import models
from config import settings

User = settings.AUTH_USER_MODEL


class CustomUser(AbstractUser):
    class Meta:
        verbose_name_plural = 'CustomUser'


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name='ユーザー',
        on_delete=models.CASCADE,
    )
    profile_image = models.ImageField(
        verbose_name='プロフィール画像',
        default='media/media/boy.png',
        upload_to='media/'
    )

    def __str__(self):
        return f'{self.user.username} Profile'