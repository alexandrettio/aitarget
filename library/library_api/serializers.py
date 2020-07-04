
from rest_framework import serializers

from .models import Author, Book, Subscriber


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'middle_name']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'language', 'publication_year', 'author']


class SubscriberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['name', 'surname', 'middle_name', 'email']
