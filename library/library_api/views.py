from rest_framework import viewsets, generics
from django.db.models import Count

from .serializers import AuthorSerializer, BookSerializer, SubscriberSerializer
from .models import Author, Book, Subscriber


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class SearchList(generics.ListAPIView):
    queryset = Book.objects.filter()
    serializer_class = BookSerializer

    def get_queryset(self):
        authors_count = self.request.query_params.get('authors_count', 10)
        return Book.objects.annotate(num_authors=Count('author')).filter(num_authors=authors_count)
