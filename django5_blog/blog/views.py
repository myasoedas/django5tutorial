from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )


def post_detail(request, id):
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )


def author_posts(request, author_id):
    """Публикации конкретного автора."""
    author = get_object_or_404(User, id=author_id)
    posts = Post.published.filter(author=author, status=Post.Status.PUBLISHED)
    return render(request, 'blog/author_posts.html',
                  {'author': author, 'posts': posts})
