from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import Book, ReadingGoal


class BookSerializer(serializers.ModelSerializer):
    progress = serializers.CharField(read_only=True)

    class Meta:
        model = Book
        fields = "__all__"


class ReadingGoalSerializer(serializers.ModelSerializer):
    progress = serializers.CharField(read_only=True)

    class Meta:
        model = ReadingGoal
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
        read_only_fields = ["id"]
