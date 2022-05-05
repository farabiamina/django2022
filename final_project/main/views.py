from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Profile, Genre, Publisher, Book, Publications, Comment, License, Article, Author
from main.serializers import ProfileSerializer, GenreSerializer, PublisherSerializer, BookSerializer, CommentSerializer, LicenseSerializer, ArticleSerializer, AuthorSerializer

from main.models import Profile
from main.serializers import ProfileSerializer
# Create your views here.
import logging
from rest_framework.permissions import IsAuthenticated, IsAdminUser

logger = logging.getLogger('main')


@api_view(['GET', 'POST'])
def profiles(request):
    if request.method == 'GET':
        profiles_list = Profile.objects.all()
        serializer = ProfileSerializer(profiles_list, many=True)
        logger.info("request was sent")
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("request was sent")
            return Response(serializer.data)
        logger.error('Could\'t perform request')
        return Response(serializer.errors, status=400)


@csrf_exempt
@api_view(['PUT', 'DELETE'])
def profile(request, profile_id):
    if request.method == 'PUT':
        profiles_list = Profile.objects.all()
        this_profile = get_object_or_404(profiles_list, pk=profile_id)
        serializer = ProfileSerializer(this_profile)
        logger.info("request was sent")
        return Response(serializer.data)
    elif request.method == 'DELETE':
        profiles_list = Profile.objects.all()
        this_profile = get_object_or_404(profiles_list, pk=profile_id)
        this_profile.delete()
        logger.info("request was sent")
        return Response({'message': 'deleted'}, status=204)


class GenreListAPIView(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request):
        genre_list = Genre.objects.all()
        serializer = GenreSerializer(genre_list, many=True)
        logger.info("request was sent")
        return Response(serializer.data)
    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("request was sent")
            return Response(serializer.data)
        logger.error('Could\'t perform request')
        return Response(serializer.errors, status=400)


class GenreAPIView(APIView):
    def put(self, request, genre_id):
        genre_list = Genre.objects.all()
        this_genre = get_object_or_404(genre_list, pk=genre_id)
        serializer = GenreSerializer(instance=this_genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("request was sent")
            return Response(serializer.data)
        logger.error('Could\'t perform request')
        return Response(serializer.errors)
    def delete(self, request, genre_id):
        genre_list = Genre.objects.all()
        this_genre = get_object_or_404(genre_list, pk=genre_id)
        this_genre.delete()
        logger.info("request was sent")
        return Response({'message': 'deleted'}, status=204)


class PublishersAPIView(APIView):
    def get(self, request):
        publisher_list = Publisher.objects.all()
        serializer = PublisherSerializer(publisher_list, many=True)
        logger.info("request was sent")
        return Response(serializer.data)
    def post(self, request):
        serializer = PublisherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("request was sent")
            return Response(serializer.data)
        logger.error('Could\'t perform request')
        return Response(serializer.errors, status=400)


class PublisherAPIView(APIView):
    def put(self, request, pub_id):
        publisher_list = Publisher.objects.all()
        this_pub = get_object_or_404(publisher_list, pk=pub_id)
        serializer = PublisherSerializer(instance=this_pub, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("request was sent")
            return Response(serializer.data)
        logger.error('Could\'t perform request')
        return Response(serializer.errors)
    def delete(self, request, pub_id):
        publisher_list = Publisher.objects.all()
        this_pub = get_object_or_404(publisher_list, pk=pub_id)
        this_pub.delete()
        logger.info("request was sent")
        return Response({'message': 'deleted'}, status=204)

    permission_classes = (IsAuthenticated,)


class BookViewSet(viewsets.ViewSet):
    def books_author(self, request):
        queryset = Book.book_objects.all()
        serializer = BookSerializer(queryset, many=True)
        logger.info("request was sent")
        return Response(serializer.data)
    def books_genre(self, request):
        queryset = Book.book_genre_objects.all()
        serializer = BookSerializer(queryset, many=True)
        logger.info("request was sent")
        return Response(serializer.data)
    def books(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        logger.info("request was sent")
        return Response(serializer.data)

    def add_book(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("request was sent")
            return Response(serializer.data)
        logger.error('Could\'t perform request')
        return Response(serializer.errors, status=400)

    def update_book(self, request, book_id=None):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk=book_id)
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("request was sent")
            return Response(serializer.data)
        logger.error('Could\'t perform request')
        return Response(serializer.errors, status=400)

    def delete_book(self, request, book_id=None):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk=book_id)
        book.delete()
        logger.info("request was sent")
        return Response({'message': 'deleted'}, status=204)\

    permission_classes = (IsAuthenticated,)

class CommentsViewSet(viewsets.ViewSet):
    def books_comment(self, request):
        queryset = Comment.books_comment_objects.all()
        serializer = CommentSerializer(queryset, many=True)
        logger.info("request was sent")
        return Response(serializer.data)

    def comments(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        logger.info("request was sent")
        return Response(serializer.data)

    def add_comment(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("request was sent")
            return Response(serializer.data)
        logger.error('Could\'t perform request')
        return Response(serializer.errors, status=400)

    def update_comment(self, request, comment_id=None):
        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, pk=comment_id)
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("request was sent")
            return Response(serializer.data)
        logger.error('Could\'t perform request')
        return Response(serializer.errors, status=400)

    def delete_comment(self, request, comment_id=None):
        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, pk=comment_id)
        comment.delete()
        logger.info("request was sent")
        return Response({'message': 'deleted'}, status=204)

    permission_classes = (IsAuthenticated,)


class LicenseViewSet(viewsets.ViewSet):
    def get_queryset(self):
        return License.objects.all()

    def licenses(self, request):
        serializer = LicenseSerializer(self.get_queryset(), many=True)
        logger.info("request was sent")
        return Response(serializer.data)

    def add_license(self, request):
        serializer = LicenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("request was sent")
            return Response(serializer.data)
        logger.error('Could\'t perform request')
        return Response(serializer.errors, status=400)

    def update_license(self, request, license_id=None):
        queryset = License.objects.all()
        license = get_object_or_404(queryset, pk=license_id)
        serializer = LicenseSerializer(instance=license, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("request was sent")
            return Response(serializer.data)
        logger.error('Could\'t perform request')
        return Response(serializer.errors, status=400)

    def delete_license(self, request, license_id=None):
        queryset = License.objects.all()
        license = get_object_or_404(queryset, pk=license_id)
        license.delete()
        logger.info("request was sent")
        return Response({'message': 'deleted'}, status=204)

    permission_classes = (IsAuthenticated,)


class ArticleViewSet(viewsets.ViewSet):
    def get_queryset(self):
        return Article.objects.all()

    def john_article(self, request):
        queryset = Article.john_objects.all()
        serializer = ArticleSerializer(queryset, many=True)
        logger.info("request was sent")
        return Response(serializer.data)

    def articles(self, request):
        serializer = ArticleSerializer(self.get_queryset(), many=True)
        logger.info("request was sent")
        return Response(serializer.data)

    def add_article(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("request was sent")
            return Response(serializer.data)
        logger.error('Could\'t perform request')
        return Response(serializer.errors, status=400)

    def update_article(self, request, article_id=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=article_id)
        serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("request was sent")
            return Response(serializer.data)
        logger.error('Could\'t perform request')
        return Response(serializer.errors, status=400)

    def delete_article(self, request, article_id=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=article_id)
        article.delete()
        return Response({'message': 'deleted'}, status=204)

    permission_classes = (IsAuthenticated,)


class AuthorViewSet(viewsets.ViewSet):
    def get_queryset(self):
        return Author.objects.all()

    def authors(self, request):
        serializer = AuthorSerializer(self.get_queryset(), many=True)
        logger.info("request was sent")
        return Response(serializer.data)

    def add_author(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("request was sent")
            return Response(serializer.data)
        logger.error('Could\'t perform request')
        return Response(serializer.errors, status=400)

    def update_author(self, request, author_id=None):
        queryset = Author.objects.all()
        author = get_object_or_404(queryset, pk=author_id)
        serializer = AuthorSerializer(instance=author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("request was sent")
            return Response(serializer.data)
        logger.error('Could\'t perform request')
        return Response(serializer.errors, status=400)

    def delete_author(self, request, author_id=None):
        queryset = Author.objects.all()
        article = get_object_or_404(queryset, pk=author_id)
        article.delete()
        return Response({'message': 'deleted'}, status=204)