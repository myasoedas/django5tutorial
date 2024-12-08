# Generated by Django 5.0.10 on 2024-12-08 12:18

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={
                "ordering": ["-publish"],
                "verbose_name": "Пост",
                "verbose_name_plural": "Посты",
            },
        ),
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="Добавьте изображение для поста (опционально)",
                null=True,
                upload_to="posts/images/",
                verbose_name="Изображение",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="blog_posts",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="body",
            field=models.TextField(verbose_name="Содержание"),
        ),
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Создан"),
        ),
        migrations.AlterField(
            model_name="post",
            name="publish",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Дата публикации"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                max_length=250, unique_for_date="publish", verbose_name="Слаг"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="status",
            field=models.CharField(
                choices=[("DF", "Черновик"), ("PB", "Опубликовано")],
                default="DF",
                max_length=2,
                verbose_name="Статус",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=250, verbose_name="Заголовок"),
        ),
        migrations.AlterField(
            model_name="post",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="Обновлен"),
        ),
    ]
