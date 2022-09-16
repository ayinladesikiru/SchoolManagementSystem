from django.contrib import admin


# Register your models here.
from sms.models import Student, Staff


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_of_birth'
    list_display = ['first_name', 'middle_name', 'last_name', 'other_student_details', 'gender']
    list_editable = ['other_student_details']
    search_fields = ['first_name']


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_of_birth'
    list_display = ['first_name', 'last_name', 'job_title', 'phone_number', 'email_address', 'other_staff_details']
    list_editable = ['other_staff_details']
    search_fields = ['email_address']

