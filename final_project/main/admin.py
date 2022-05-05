from django.contrib import admin

from django.contrib import admin
from main.models import Profile, Genre, Publisher, Book, Publications, Comment, License, Article, Author

from main.models import Profile


admin.site.register(Profile)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(License)
admin.site.register(Article)
admin.site.register(Author)
