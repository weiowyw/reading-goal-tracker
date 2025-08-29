import pytest
from django.contrib.auth.models import User
from books.models import Book, ReadingGoal
from books.api.serializers import BookSerializer, ReadingGoalSerializer, UserSerializer
from datetime import date


@pytest.mark.django_db
def test_book_serializer():
    user = User.objects.create_user(username="testuser")
    book = Book.objects.create(
        user=user,
        title="Test Book",
        start_date=date.today(),
        total_pages=100,
        pages_read=50,
    )
    serializer = BookSerializer(book)
    data = serializer.data
    assert data["title"] == "Test Book"
    assert data["progress"] == 50.0
    assert data["pages_read"] == 50


@pytest.mark.django_db
def test_reading_goal_serializer():
    user = User.objects.create_user(username="testuser")
    goal = ReadingGoal.objects.create(
        user=user, year=2025, month=8, target_books=10, completed_books=3
    )
    serializer = ReadingGoalSerializer(goal)
    data = serializer.data
    assert data["year"] == 2025
    assert data["month"] == 8
    assert data["progress"] == 30.0


@pytest.mark.django_db
def test_user_serializer():
    user = User.objects.create_user(username="testuser", email="a@test.com")
    serializer = UserSerializer(user)
    data = serializer.data
    assert data["username"] == "testuser"
    assert data["email"] == "a@test.com"
