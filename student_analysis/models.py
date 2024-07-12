# models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    roll_number = models.CharField(max_length=20, unique=True)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username

    




class SubjectData(models.Model):
    seat_no = models.CharField(max_length=50)
    student_name = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=100)
    score = models.FloatField()


    def __str__(self):
        return f"{self.student_name} - {self.subject_name}"

from django.db import models

class StudentPerformanceData(models.Model):
    seat_no = models.CharField(max_length=100)
    student_name = models.CharField(max_length=255)
    performance_level = models.CharField(max_length=50)
    subject_name = models.CharField(max_length=255)
    score = models.FloatField()
    
    low_marks_subjects = models.ManyToManyField(SubjectData, related_name='low_marks_subjects')

    def __str__(self):
        return f"{self.student_name} - {self.performance_level}"
    

class StudyMaterial(models.Model):
    title = models.CharField(max_length=100)
    links = models.URLField()
    performance_level = models.CharField(max_length=100)
    sms_recommendations = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_materials')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_materials', null=True, blank=True)

    def __str__(self):
        return self.title