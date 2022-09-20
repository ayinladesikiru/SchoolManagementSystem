from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from sms.models import Student, Staff
from sms.serializer import StudentSerializer, StaffSerializer


def student_list(request):
    students = Student.objects.all()
    return render(request, 'sms/student-list.html', {'students': list(students)})


def student_details(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'sms/student-detail.html', {'student': student})


def staff_list(request):
    staffs = Staff.objects.all()
    return render(request, 'sms/staff-list.html', {'staffs': staffs})


def staff_details(request, pk):
    try:
        staff = get_object_or_404(Staff, pk=pk)
        return render(request, 'sms/staff-details.html', {'staff': staff})
    except Staff.DoesNotExist:
        return render(request, 'sms/404.html')


@api_view(['GET', 'POST'])
def student_api(request):
    queryset = Student.objects.all()
    serializer = StudentSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def staffs_api(request):
    queryset = Staff.objects.all()
    serializer = StaffSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def student_detail_api(request, pk):
    student = get_object_or_404(Student, pk=pk)
    serializer = StudentSerializer(student)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def staff_detail_api(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    serializer = StaffSerializer(staff)
    return Response(serializer.data)
