from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer, ScheduleSerializer, SavedScheduleSerializer, SavedScheduleListSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Schedule, SavedSchedule, Category


class CreateCategoryApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetCategoryApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):

        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetAllCategoryApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        category = Category.objects.all()

        serializer = CategorySerializer(category, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


# views for schedule

class CreateScheduleApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = ScheduleSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save(user_id=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": str(e)})


class DeleteScheduleApiView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            schedule = Schedule.objects.get(pk=pk, user_id=request.user)

            if schedule:
                schedule.delete()
                return Response({"message": "Schedule was Successfully deleted"})

        except Schedule.DoesNotExist:
            return Response({"error": "Schedule Not Found"}, status=status.HTTP_404_NOT_FOUND)


class UpdateScheduleApiView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            schedule = Schedule.objects.get(pk=pk, user_id=request.user)

            serializer = ScheduleSerializer(schedule, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save(user_id=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Schedule.DoesNotExist:
            return Response({"error": "Schedule Not Found"}, status=status.HTTP_404_NOT_FOUND)


class GetScheduleApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        try:
            schedule = Schedule.objects.get(pk=pk)

            serializer = ScheduleSerializer(schedule)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Schedule.DoesNotExist:
            return Response({"error": "Schedule Not Found"}, status=status.HTTP_404_NOT_FOUND)


class GetAllScheduleApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            schedules = Schedule.objects.all()

            serializer = ScheduleSerializer(schedules, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Schedule.DoesNotExist:
            return Response({"error": "Schedule Not Found.!"}, status=status.HTTP_404_NOT_FOUND)


# views for saved_schedule

class CreateSavedScheduleApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # schedule = Schedule.objects.get(pk=pk)

            serializer = SavedScheduleSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save(user_id=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Schedule.DoesNotExist:
            return Response({"error": "Schedule Not Found.!"}, status=status.HTTP_404_NOT_FOUND)


class GetSavedScheduleApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:

            saved_schedule = SavedSchedule.objects.filter(user_id=request.user)
            serializer = SavedScheduleListSerializer(saved_schedule, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except SavedSchedule.DoesNotExist:
            return Response({"error": "SavedSchedule Not Found.!"}, status=status.HTTP_404_NOT_FOUND)


class DeleteSavedSchedule(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            saved_schedule = SavedSchedule.objects.get(pk=pk, user_id=request.user)

            if saved_schedule:
                saved_schedule.delete()
                return Response({"message": "Saved_Schedule was Successfully deleted"})

        except SavedSchedule.DoesNotExist:
            return Response({"error": "Saved_Schedule Not Found"}, status=status.HTTP_404_NOT_FOUND)






