from django.contrib import admin
from django.urls import path
from main.views import (profile, profiles,
                        GenreListAPIView, GenreAPIView, PublishersAPIView, PublisherAPIView,
                        BookViewSet, CommentsViewSet, LicenseViewSet, ArticleViewSet, AuthorViewSet)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/', profiles),
    path('profiles/<int:profile_id>', profile),
    path('genres/', GenreListAPIView.as_view()),
    path('genres/<int:genre_id>', GenreAPIView.as_view()),
    path('publishers/', PublishersAPIView.as_view()),
    path('publishers/<int:pub_id>', PublisherAPIView.as_view()),
    path('books/', BookViewSet.as_view({'get': 'books', 'post': 'add_book'})),
    path('books/<int:book_id>', BookViewSet.as_view({'put': 'update_book', 'delete': 'delete_book'})),
    path('comments/', CommentsViewSet.as_view({'get': 'comments', 'post': 'add_comment'})),
    path('comments/<int:comment_id>', CommentsViewSet.as_view({'put': 'update_comment', 'delete': 'delete_comment'})),
    path('licenses/', LicenseViewSet.as_view({'get': 'licenses', 'post': 'add_license'})),
    path('licenses/<int:license_id>', LicenseViewSet.as_view({'put': 'update_license', 'delete': 'delete_license'})),
    path('articles/', ArticleViewSet.as_view({'get': 'articles', 'post': 'add_article'})),
    path('articles/<int:article_id>', ArticleViewSet.as_view({'put': 'update_article', 'delete': 'delete_article'})),
    path('authors/', AuthorViewSet.as_view({'get': 'authors', 'post': 'add_author'})),
    path('authors/<int:author_id>', AuthorViewSet.as_view({'put': 'update_author', 'delete': 'delete_author'})),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('book5/', BookViewSet.as_view({'get': 'books_author'})),
    path('book_horror/', BookViewSet.as_view({'get': 'books_genre'})),
    path('article_john/', ArticleViewSet.as_view({'get': 'john_article'})),
    path('comment4/', CommentsViewSet.as_view({'get': 'books_comment'})),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


