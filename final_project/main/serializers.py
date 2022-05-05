from abc import ABC

from rest_framework.serializers import Serializer, ModelSerializer, StringRelatedField
from main.models import Profile, Genre, Publisher, Book, Publications, Comment, License, Article, Author
from rest_framework import serializers

class ProfileSerializer(Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    is_author = serializers.BooleanField(default=False)
    image = serializers.ImageField()
    comments = StringRelatedField(many=True)
    licenses = StringRelatedField(many=True)

    class Meta:
        model = Profile
        fields = ['username', 'email']


class AuthorSerializer(ProfileSerializer):
    books = StringRelatedField(many=True)
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']

class GenreSerializer(Serializer):
    genre = serializers.CharField(max_length=30)

    class Meta:
        model = Genre
        fields = '__all__'


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class BookSerializer(ModelSerializer):
    genre = GenreSerializer(read_only=True, many=True)
    comments = StringRelatedField(many=True)
    licenses = StringRelatedField(many=True)
    articles = StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class PublicationSerializer(ModelSerializer):
    class Meta:
        model = Publications
        fields = '__all__'


class CommentSerializer(PublicationSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LicenseSerializer(PublicationSerializer):
    class Meta:
        model = License
        fields = '__all__'


class ArticleSerializer(PublicationSerializer):
    class Meta:
        model = Article
        fields = '__all__'
