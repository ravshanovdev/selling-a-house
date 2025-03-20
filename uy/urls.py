from django.urls import path
from .views import CreateCategoryApiView, CreateScheduleApiView, DeleteScheduleApiView, UpdateScheduleApiView, \
    GetScheduleApiView, GetAllScheduleApiView


urlpatterns = [
    path('create_category/', CreateCategoryApiView.as_view(), ),
    path('create_schedule/', CreateScheduleApiView.as_view(), ),
    path('delete_schedule/<int:pk>/', DeleteScheduleApiView.as_view(), ),
    path('update_schedule/<int:pk>/', UpdateScheduleApiView.as_view(), ),
    path('get_schedule/<int:pk>/', GetScheduleApiView.as_view(), ),
    path('get_all_schedule/', GetAllScheduleApiView.as_view(), ),

]


