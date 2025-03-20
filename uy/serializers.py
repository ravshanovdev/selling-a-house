from rest_framework import serializers
from .models import Category, Schedule, SavedSchedule
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'phone']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)
    # category = CategorySerializer()

    class Meta:
        model = Schedule
        fields = "__all__"


class SavedScheduleSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)

    class Meta:
        model = SavedSchedule
        fields = "__all__"


class SavedScheduleListSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)
    schedule = ScheduleSerializer(read_only=True)

    class Meta:
        model = SavedSchedule
        fields = "__all__"


