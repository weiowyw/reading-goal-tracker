from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    total_pages = models.PositiveIntegerField()
    pages_read = models.PositiveIntegerField(default=0)

    def progress(self):
        return (self.pages_read / self.total_pages) * 100 if self.total_pages else 0

    def __str__(self):
        return f"{self.title} ({self.user.username})"


class ReadingGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField(null=True, blank=True)
    target_books = models.PositiveIntegerField()
    completed_books = models.PositiveIntegerField(default=0)

    def progress(self):
        return (self.completed_books / self.target_books) * 100 if self.target_books else 0

    def __str__(self):
        return f"Goal {self.year}-{self.month or 'Full year'} for {self.user.username}"
