from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from .models import Post
from django.conf import settings


def get_image_url(image_field, request):
    """
    Возвращает абсолютный URL изображения или URL изображения по умолчанию.
    """
    if image_field and image_field.name:  # Проверка наличия имени файла
        return request.build_absolute_uri(image_field.url)
    return request.build_absolute_uri(settings.STATIC_URL + "img/default-og-image.jpg")


def post_list(request):
    """Список всех опубликованных постов."""
    posts = Post.published.all()
    context = {
        'posts': posts,
        'page_title': "Список публикаций",
        'page_description': "Читайте последние публикации на нашем блоге. Узнайте больше на интересные темы.",
        'page_og_author': "Администратор",
        'page_og_image_url': get_image_url(None, request),  # Используем изображение по умолчанию
        'page_og_image_alt': "Общее изображение для страницы списка публикаций",
        'page_og_site_name': "Мой блог",
        'page_og_locale': "ru_RU",
        'page_robots': "index, follow",
    }
    return render(request, 'blog/post/list.html', context)


def post_detail(request, id):
    """Детальная информация о публикации."""
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )
    og_image_url = get_image_url(post.image, request)
    context = {
        'post': post,
        'page_title': post.title,
        'page_description': post.body[:160],  # Ограничение описания до 160 символов
        'page_og_author': post.author.username,
        'page_og_image_url': og_image_url,
        'page_og_image_alt': f"Изображение для публикации {post.title}",
        'page_og_site_name': "Мой блог",
        'page_og_locale': "ru_RU",
        'page_robots': "index, follow",
    }
    return render(request, 'blog/post/detail.html', context)


def author_posts(request, author_id):
    """Публикации конкретного автора."""
    author = get_object_or_404(User, id=author_id)
    posts = Post.published.filter(author=author)
    # Получаем изображение автора или используем изображение по умолчанию
    og_image_url = get_image_url(posts[0].image if posts.exists() else None, request)
    context = {
        'author': author,
        'posts': posts,
        'page_title': f"Публикации автора {author.username}",
        'page_description': f"Список публикаций, созданных пользователем {author.username}.",
        'page_og_author': author.username,
        'page_og_image_url': og_image_url,
        'page_og_image_alt': f"Изображение профиля автора {author.username}",
        'page_og_site_name': "Мой блог",
        'page_og_locale': "ru_RU",
        'page_robots': "index, follow",
    }
    return render(request, 'blog/author_posts.html', context)
