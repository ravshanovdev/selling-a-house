from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer, ScheduleSerializer, SavedScheduleSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Schedule


class CreateCategoryApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
