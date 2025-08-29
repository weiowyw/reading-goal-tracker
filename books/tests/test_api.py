import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from books.models import Book
from datetime import date


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser")


@pytest.mark.django_db
def test_get_books(api_client, user):
    Book.objects.create(user=user, title="Book1", start_date=date.today(), total_pages=100)
    response = api_client.get("/books/api/books/")
    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_create_book_api(api_client, user):
    data = {
        "user": user.id,
        "title": "New Book",
        "start_date": str(date.today()),
        "total_pages": 120,
        "pages_read": 10
    }
    response = api_client.post("/books/api/books/", data)
    assert response.status_code == 201
    assert response.data['title'] == "New Book"
    assert response.data['pages_read'] == 10
