from rest_framework import serializers

from sms.models import Student, Staff


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        # fields = ['date_of_birth', 'first_name', 'last_name', 'job_title', 'phone_number', 'email_address', 'other_staff_details']
        fields = "__all__"
