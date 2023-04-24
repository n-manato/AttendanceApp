from django.db import models
from django.utils import timezone

#生徒の名前(親)
class Student(models.Model):
    name = models.CharField(max_length=50)
    number = models.SmallIntegerField(null=True,blank=True)

    def __str__(self):
        return self.name

#先生の名前
class Teacher(models.Model):
    name = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=50, blank=True)
    period = models.CharField(max_length=50, blank=True)#何時限目

    def __str__(self):
        return self.name
    
class AttendanceInfo(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    attendance = models.CharField(max_length=50, blank=True,)
    date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.attendance