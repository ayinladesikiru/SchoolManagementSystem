from django.urls import path
from . import views

app_name = 'sms'

urlpatterns = [
    path('student-list/', views.student_list, name='student-list'),
    path('student-details/<int:pk>/', views.student_details, name='students-details'),
    path('staff-list/', views.staff_list, name='staff-list'),
    path('staff-details/<int:pk>/', views.staff_details, name='staff-details'),
    path('students/', views.student_api, name='students-api'),
    path('staffs/', views.staffs_api, name='staffs-api'),
    path('student/<int:pk>/', views.student_detail_api, name='student-detail'),
    path('staff/<int:pk>/', views.staff_detail_api, name='staff-detail')
]
