from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    photo = models.ImageField(upload_to = 'avatars/%Y/%m/%d/', blank=False, verbose_name='Фото')
    bio = models.TextField(blank=True, verbose_name='О себе')

    def __str__(self):
        return f'{self.user}'
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ['-id', '-user']