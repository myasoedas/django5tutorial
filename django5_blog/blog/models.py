from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    """Менеджер для получения опубликованных постов."""
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Черновик'
        PUBLISHED = 'PB', 'Опубликовано'

    title = models.CharField(
        max_length=250,
        verbose_name='Заголовок'
    )
    slug = models.SlugField(
        max_length=250,
        unique_for_date='publish',
        verbose_name='Слаг'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts',
        verbose_name='Автор'
    )
    body = models.TextField(
        verbose_name='Содержание'
    )
    image = models.ImageField(
        upload_to='posts/images/',
        blank=True,
        null=True,
        help_text='Добавьте изображение для поста (опционально)',
        verbose_name='Изображение'
    )
    publish = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата публикации'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создан'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Обновлен'
    )
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT,
        verbose_name='Статус'
    )

    objects = models.Manager()  # Менеджер по умолчанию
    published = PublishedManager()  # Кастомный менеджер

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        """Возвращает абсолютный URL для отображения поста."""
        return reverse('blog:post_detail', args=[self.id])

    def __str__(self):
        return self.title
