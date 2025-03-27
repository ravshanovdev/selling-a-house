from django.urls import path
from .views import CreateCategoryApiView, CreateScheduleApiView, DeleteScheduleApiView, UpdateScheduleApiView, \
    GetScheduleApiView, GetAllScheduleApiView, CreateSavedScheduleApiView, GetSavedScheduleApiView, DeleteSavedSchedule, \
    GetCategoryApiView, GetAllCategoryApiView, GetScheduleByCategoryIDApiView, CreateReviewApiView, GetReviewApiView


urlpatterns = [
    path('create_category/', CreateCategoryApiView.as_view(), ),
    path('create_schedule/', CreateScheduleApiView.as_view(), ),
    path('delete_schedule/<int:pk>/', DeleteScheduleApiView.as_view(), ),
    path('update_schedule/<int:pk>/', UpdateScheduleApiView.as_view(), ),
    path('get_schedule/<int:pk>/', GetScheduleApiView.as_view(), ),
    path('get_all_schedule/', GetAllScheduleApiView.as_view(), ),
    path('create_saved_schedule/', CreateSavedScheduleApiView.as_view(), ),
    path("get_saved_schedule/", GetSavedScheduleApiView.as_view(), ),
    path('delete_saved_schedule/<int:pk>/', DeleteSavedSchedule.as_view(), ),
    path('get_category_by_id/<int:pk>/', GetCategoryApiView.as_view(), ),
    path('get_all_category/', GetAllCategoryApiView.as_view(), ),
    path('get_schedule_by_category_id/<int:pk>/', GetScheduleByCategoryIDApiView.as_view(), ),
    path('create_review/', CreateReviewApiView.as_view(), ),
    path('get_review/<int:pk>/', GetReviewApiView.as_view(), ),


]


