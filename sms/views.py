from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from sms.models import Student, Staff


def student_list(request):
    students = Student.objects.all()
    return render(request, 'sms/student-list.html', {'students': list(students)})


def student_details(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'sms/student-detail.html', {'student': student})


def index(request):
    return HttpResponse("Welcome to School Management portal")


def staff_list(request):
    staffs = Staff.objects.all()
    return render(request, 'sms/staff-list.html', {'staffs': staffs})


def staff_details(request, pk):
    try:
        staff = get_object_or_404(Staff, pk=pk)
        return render(request, 'sms/staff-details.html', {'staff': staff})
    except Staff.DoesNotExist:
        return render(request, 'sms/404.html')