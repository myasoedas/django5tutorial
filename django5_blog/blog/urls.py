from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Список всех публикаций
    path('', views.post_list, name='post_list'),

    # Детальная страница поста (по ID)
    path('<int:id>/', views.post_detail, name='post_detail'),

    # Посты определенного автора
    path('author/<int:author_id>/', views.author_posts, name='author_posts'),
]

# Обработка медиа-файлов в режиме DEBUG
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
