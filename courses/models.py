from datetime import timezone
from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.TextField(max_length=255)
    description = models.TextField()
    duration = models.DurationField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    published_date = models.DateField(null=True, blank=True)  # Published date
    
class Instructor(models.Model):
    name = models.TextField(max_length=255)
    bio = models.TextField()

class Student(models.Model):
    name = models.TextField(max_length=255)
    email = models.EmailField()

class CourseEnrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='courses')
    student = models.ForeignKey(Student,on_delete=models.PROTECT, related_name='courses')


