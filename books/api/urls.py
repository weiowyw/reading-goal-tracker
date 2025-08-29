from rest_framework.routers import DefaultRouter
from django.urls import path, include

from books.views import BookViewSet, UserViewSet

app_name = "books"

router = DefaultRouter()
router.register(r"books", BookViewSet, basename="book")
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
]
