from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet, BookViewSet, SubscriberViewSet, SearchList

router = DefaultRouter()
router.register('api/v1/authors', AuthorViewSet)
router.register('api/v1/books', BookViewSet)
router.register('api/v1/subscribers', SubscriberViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/search', SearchList.as_view())
]