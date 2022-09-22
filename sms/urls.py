from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter

app_name = 'sms'

router = SimpleRouter()
router.register('students', views.StudentViewSet)
router.register('staffs', views.StaffViewSet)

urlpatterns = [
    path('', include(router.urls))
]
