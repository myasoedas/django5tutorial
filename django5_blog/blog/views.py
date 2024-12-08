from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.utils.html import escape
from .models import Post


def post_list(request):
    """Список всех опубликованных постов."""
    posts = Post.published.all()
    context = {
        'posts': posts,
        'page_title': "Список публикаций",
        'page_description': escape("Читайте последние публикации на нашем блоге. Узнайте больше на интересные темы."),
        'page_og_author': "Администратор",
        'page_og_image_url': request.build_absolute_uri("/static/img/default-og-image.jpg"),
        'page_og_image_alt': escape("Общее изображение для страницы списка публикаций"),
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
    og_image_url = (
        request.build_absolute_uri(post.image.url)
        if post.image else request.build_absolute_uri("/static/img/default-og-image.jpg")
    )
    context = {
        'post': post,
        'page_title': escape(post.title),
        'page_description': escape(post.body[:160]),  # Ограничение описания до 160 символов
        'page_og_author': post.author.username,
        'page_og_image_url': og_image_url,
        'page_og_image_alt': escape(f"Изображение для публикации {post.title}"),
        'page_og_site_name': "Мой блог",
        'page_og_locale': "ru_RU",
        'page_robots': "index, follow",
    }
    return render(request, 'blog/post/detail.html', context)


def author_posts(request, author_id):
    """Публикации конкретного автора."""
    author = get_object_or_404(User, id=author_id)
    posts = Post.published.filter(author=author)
    og_image_url = request.build_absolute_uri("/static/img/default-og-image.jpg")  # Замените на URL аватара, если доступен
    context = {
        'author': author,
        'posts': posts,
        'page_title': escape(f"Публикации автора {author.username}"),
        'page_description': escape(f"Список публикаций, созданных пользователем {author.username}."),
        'page_og_author': author.username,
        'page_og_image_url': og_image_url,
        'page_og_image_alt': escape(f"Изображение профиля автора {author.username}"),
        'page_og_site_name': "Мой блог",
        'page_og_locale': "ru_RU",
        'page_robots': "index, follow",
    }
    return render(request, 'blog/author_posts.html', context)
