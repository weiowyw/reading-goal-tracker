from datetime import date, timedelta

from django.contrib.auth.models import User
from django.db.models import Sum
from rest_framework import viewsets, decorators, response
from rest_framework.permissions import IsAdminUser

from .api.serializers import BookSerializer, ReadingGoalSerializer, UserSerializer
from .models import Book, ReadingGoal

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @decorators.action(detail=False, methods=['get'])
    def weekly_stats(self, request):
        today = date.today()
        week_start = today - timedelta(days=today.weekday())
        books = self.queryset.filter(date_finished__gte=week_start)
        total_pages = books.aggregate(Sum('pages'))['pages__sum'] or 0
        return response.Response({
            "week_start": week_start,
            "total_books": books.count(),
            "total_pages": total_pages
        })


class ReadingGoalViewSet(viewsets.ModelViewSet):
    queryset = ReadingGoal.objects.all()
    serializer_class = ReadingGoalSerializer

    @decorators.action(detail=True, methods=['get'])
    def progress(self, request, pk=None):
        goal = self.get_object()
        books = Book.objects.filter(user=goal.user, date_finished__year=goal.year)
        pages_read = books.aggregate(Sum('pages'))['pages__sum'] or 0
        progress_percent = (pages_read / goal.pages_target * 100) if goal.pages_target else 0
        return response.Response({
            "goal": goal.pages_target,
            "pages_read": pages_read,
            "progress_percent": round(progress_percent, 2)
        })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserBooksViewSet(viewsets.ModelViewSet):
    @decorators.action(detail=False, methods=['get'])
    def my_books(self, request):
        user = request.user
        books = Book.objects.filter(user=user)
        serializer = BookSerializer(books, many=True)
        return response.Response(serializer.data)

