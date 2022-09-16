from django.urls import path
from . import views

app_name = 'sms'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('student-list/', views.student_list, name='student-list'),
    path('student-details/<int:pk>/', views.student_details, name='students-details'),
    path('staff-list/', views.staff_list, name='staff-list'),
    path('staff-details/<int:pk>/', views.staff_details, name='staff-details')
]
