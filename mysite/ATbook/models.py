from django.db import models
from django.utils import timezone

#生徒の名前(親)
class Student(models.Model):
    name = models.CharField(max_length=50)
    number = models.SmallIntegerField(null=True)

    def __str__(self):
        return self.name

class Period(models.Model):
    period = models.CharField(max_length=50)#前期・後期

    def __str__(self):
        return self.period
    
class HourAttend(models.Model):
    hour = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.hour



#先生の名前(親)
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50, blank=True)
    period = models.ForeignKey(Period, on_delete=models.SET_NULL, null=True, related_name='related_period')
    time = models.ForeignKey(HourAttend, on_delete=models.SET_NULL, null=True, related_name='related_hour')

    def __str__(self):
        return self.name
    



class Attend(models.Model):
    kind = models.CharField(max_length=50,blank=True)
    
    def __str__(self):
        return self.kind


    

#出席情報
class AttendanceInfo(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, related_name='related_student')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='related_teacher')
    attendance = models.ForeignKey(Attend, on_delete=models.SET_NULL, null=True, related_name='related_attendance')
    time = models.ForeignKey(HourAttend, on_delete=models.SET_NULL, null=True, related_name='related_hourattend')
    date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.student.name
    