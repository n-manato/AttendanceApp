from django.db import models
from django.utils import timezone

#生徒の名前(親)
class Student(models.Model):
    name = models.CharField(max_length=50)
    number = models.SmallIntegerField(null=True,blank=True)

    def __str__(self):
        return self.name

class Period(models.Model):
    period = models.CharField(max_length=50, blank=True)#何時限目

#先生の名前(親)
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50, blank=True)
    period = models.ForeignKey(Period, on_delete=models.SET_NULL, null=True, related_name='related_period')
 

    def __str__(self):
        return self.name
    
class Attend(models.Model):
    kind = models.CharField(max_length=50, blank=True)

class HourAttend(models.Model):
    hr = models.ForeignKey(Attend, on_delete=models.SET_NULL, null=True, related_name='related_hr')
    hour_1 = models.ForeignKey(Attend, on_delete=models.SET_NULL, null=True, related_name='related_hour_1')
    hour_2 = models.ForeignKey(Attend, on_delete=models.SET_NULL, null=True, related_name='related_hour_2')
    hour_3 = models.ForeignKey(Attend, on_delete=models.SET_NULL, null=True, related_name='related_hour_3')
    hour_4 = models.ForeignKey(Attend, on_delete=models.SET_NULL, null=True, related_name='related_hour_4')
    hour_5 = models.ForeignKey(Attend, on_delete=models.SET_NULL, null=True, related_name='related_hour_5')
    hour_6 = models.ForeignKey(Attend, on_delete=models.SET_NULL, null=True, related_name='related_hour_6')
    hour_7 = models.ForeignKey(Attend, on_delete=models.SET_NULL, null=True, related_name='related_hour_7')
    hour_8 = models.ForeignKey(Attend, on_delete=models.SET_NULL, null=True, related_name='related_hour_8')
    def __str__(self):
        return self.hr

#出席情報
class AttendanceInfo(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, related_name='related_student')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='related_teacher')
    attendance = models.ForeignKey(HourAttend, on_delete=models.SET_NULL, null=True, related_name='related_attendance')
    date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.student.name
    