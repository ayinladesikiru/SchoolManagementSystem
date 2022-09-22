from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from sms.models import Student, Staff
from sms.serializer import StudentSerializer, StaffSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Student, Staff


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StaffViewSet(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
