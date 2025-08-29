import pytest
from django.contrib.auth.models import User
from books.models import Book, ReadingGoal
from datetime import date


@pytest.mark.django_db
def test_book_progress():
    user = User.objects.create_user(username="testuser")
    book = Book.objects.create(
        user=user,
        title="Test Book",
        start_date=date.today(),
        total_pages=100,
        pages_read=25,
    )
    assert book.progress() == "25%"


@pytest.mark.django_db
def test_book_progress_zero_total_pages():
    user = User.objects.create_user(username="testuser")
    book = Book.objects.create(
        user=user,
        title="Empty Book",
        start_date=date.today(),
        total_pages=0,
        pages_read=0,
    )
    assert book.progress() == "0%"


@pytest.mark.django_db
def test_reading_goal_progress():
    user = User.objects.create_user(username="testuser")
    goal = ReadingGoal.objects.create(
        user=user, year=2025, target_books=10, completed_books=4
    )
    assert goal.progress() == "40%"
