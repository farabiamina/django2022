from django.utils.timezone import now

from django.db import models
from django.contrib.auth.models import AbstractUser


class BookAuthorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(author=5)


class BookGenreManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(genre=8)


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(author="John Smith")


class CommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(book=4)


class Profile(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, null=True, unique=True)
    # is_author = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    image = models.ImageField(null=True, upload_to='images/')
    # books
    # my_books = models.ManyToManyField(Book)

    class Meta:
        def __str__(self):
            return self.username


class Author(Profile):
    class Meta:
        def __str__(self):
            return self.first_name + " " + self.last_name


class Genre(models.Model):
    genre = models.CharField(max_length=30)

    class Meta:
        def __str__(self):
            return self.genre


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=60, default="Almaty")
    country = models.CharField(max_length=50, default="Kazakstan")
    website = models.URLField(null=True)

    class Meta:
        def __str__(self):
            return self.name + self.city


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books', null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, related_name='books')
    genre = models.ManyToManyField(Genre)
    publication_date = models.DateField()
    file = models.FileField(upload_to='files/', null=True)
    publication_date = models.DateField(default=now)
    book_objects = BookAuthorManager()
    book_genre_objects = BookGenreManager()
    class Meta:
        def __str__(self):
            return "'" + self.title + "' by" + self.author


class Publications(models.Model):
    publication_date = models.DateField(default=now)
    likes = models.IntegerField()

    class Meta:
        abstract = True

        def __str__(self):
            return self.id + "for " + self.book + " by" + self.user


class Comment(Publications):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments', default=1)
    text = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    books_comment_objects = CommentManager()

    class Meta:
        def __str__(self):
            return "comment " + self.id + " for " + self.book + " by " + self.profile


class License(Publications):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='licenses', default=1)
    text = models.CharField(max_length=500)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='licenses', null=True, blank=True)
    licenses = models.Manager
    class Meta:
        def __str__(self):
            return "license " + super.__str__()


class Article(Publications):
    text = models.CharField(max_length=500)
    source = models.URLField(null=True)
    author = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='articles', null=True, blank=True)
    john_objects = ArticleManager()
    objects = models.Manager()

    class Meta:
        def __str__(self):
            return "article " + super.__str__()
