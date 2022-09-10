from django.db import models

# Create your models here.

from django.db import models


# Create your models here.

class Students(models.Model):
    GENDER = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female')
    )
    student_id = models.IntegerField(primary_key=True)
    date_of_birth = models.DateField()
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    other_student_details = models.TextField(255)
    gender = models.CharField(choices=GENDER, max_length=6)


class Course_Scheduled(models.Model):
    course_schedule_id = models.IntegerField(primary_key=True)
    course_offering_id = models.ForeignKey('Course_Offered', on_delete=models.CASCADE)
    other_course_schedule_details = models.TextField(max_length=255)
    course_offered = models.ManyToOneRel('Course_Offered', on_delete=models.CASCADE, field_name='course_offered')


class Student_Course_Registrations(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    course_schedule_id = models.ForeignKey(Course_Scheduled, on_delete=models.CASCADE)
    student_course_registration = models.ManyToOneRel(Students, on_delete=models.CASCADE)
    course_scheduled = models.ManyToOneRel(Course_Scheduled, on_delete=models.CASCADE)


class Course_Offered(models.Model):
    course_offering_id = models.IntegerField(primary_key=True)
    course_offering_name = models.TextField(max_length=255)
    other_course_offering_details = models.TextField(max_length=255)


class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    date_of_birth = models.DateField()
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    job_title = models.TextField(max_length=255)
    phone_number = models.TextField(max_length=15)
    email_address = models.EmailField(unique=True)
    other_staff_details = models.TextField(max_length=255)


class Staff_Courses_Supervision(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    course_offering_id = models.ForeignKey(Course_Offered, on_delete=models.CASCADE)
    staff = models.ManyToOneRel(Staff, on_delete=models.CASCADE)


class Staff_Research_Interests(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    area_of_research_id = models.ForeignKey('Research_Projects', on_delete=models.CASCADE)
    staff = models.ManyToOneRel(Staff, on_delete=models.CASCADE)


class Research_Projects(models.Model):
    project_id = models.IntegerField(max_length=120, primary_key=True)
    area_of_research_id = models.IntegerField(max_length=120)
    project_name = models.TextField(max_length=255)
    project_description = models.TextField(max_length=255)
    other_details = models.TextField(max_length=255)


class Staff_on_Research_Projects(models.Model):
    project_id = models.ForeignKey(Research_Projects, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date_from = models.DateField(primary_key=True)
    date_to = models.DateField()
    research_projects = models.ManyToOneRel(Research_Projects, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)