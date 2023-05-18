from django.db import models
from django.urls import reverse
from Members.models import Profile
from django.conf import settings

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=55, verbose_name='Имя')
    alias = models.CharField(max_length=55, blank=True, verbose_name='Псевдоним')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    date_of_death = models.DateField(blank=True, null=True, verbose_name='Дата смерти')
    preview = models.TextField(max_length=255, verbose_name='Краткое описание')
    content = models.TextField(verbose_name='Контент')
    photo = models.ImageField(upload_to = 'authors/%Y/%m/%d/', blank=True, verbose_name='Фото')
    genres = models.ManyToManyField('Genre', blank=True, verbose_name='Жанры')
    # works = models.ManyToManyField('Work', blank=True, verbose_name='Работы')

    def get_absolute_url(self):
        return reverse('author', kwargs={'author_id': self.pk})

    def __str__(self):
        alias = f' ({self.alias})' if self.alias else ''
        return f'{self.name}{alias}'

    def get_works(self):
        return Work.objects.filter(authors__id=self.pk)
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['id',]

class AuthorComment(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='Автор')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор комментария')
    content = models.TextField(max_length=255, verbose_name='Контент')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    likes = models.ManyToManyField('Members.Profile', verbose_name='Лайки')

    def __str__(self):
        return f'{self.author}. {self.user}'
    
    class Meta:
        verbose_name = 'Комментарий к автору'
        verbose_name_plural = 'Комментарии к автору'
        ordering = ['id',]

class Genre(models.Model):
    title = models.CharField(max_length=55, verbose_name='Название')
    preview = models.TextField(max_length=255, verbose_name='Краткое описание')
    content = models.TextField(verbose_name='Контент')
    photo = models.ImageField(upload_to='genres/%Y/%m/%d/', blank=True, verbose_name='Фото')

    def get_absolute_url(self):
        return reverse('genre', kwargs={'genre_id': self.pk})

    def __str__(self):
        return f'{self.title}'
    
    def get_authors(self):
        return Author.objects.filter(genres__id=self.pk)

    def get_works(self):
        return Work.objects.filter(genres__id=self.pk)
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['id',]

class GenreComment(models.Model):
    author = models.ForeignKey('Genre', on_delete=models.CASCADE, verbose_name='Жанр')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор комментария')
    content = models.TextField(max_length=255, verbose_name='Контент')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    likes = models.ManyToManyField('Members.Profile', verbose_name='Лайки')

    def __str__(self):
        return f'{self.author}. {self.user}'
    
    class Meta:
        verbose_name = 'Комментарий к жанру'
        verbose_name_plural = 'Комментарии к жанру'
        ordering = ['id',]

class Work(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    preview = models.TextField(max_length=255, verbose_name='Описание')
    content = models.TextField(verbose_name='Контент')
    photo = models.ImageField(upload_to='works/%Y/%m/%d/', blank=True, verbose_name='Фото')
    genres = models.ManyToManyField('Genre', verbose_name='Жанры')
    authors = models.ManyToManyField('Author', verbose_name='Авторы')

    def get_absolute_url(self):
        return reverse('work', kwargs={'work_id': self.pk})

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
        ordering = ['id',]

class WorkComment(models.Model):
    author = models.ForeignKey('Work', on_delete=models.CASCADE, verbose_name='Жанр')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор комментария')
    content = models.TextField(max_length=255, verbose_name='Контент')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    likes = models.ManyToManyField('Members.Profile', verbose_name='Лайки')

    def __str__(self):
        return f'{self.author}. {self.user}'
    
    class Meta:
        verbose_name = 'Комментарий к работе'
        verbose_name_plural = 'Комментарии к работе'
        ordering = ['id',]