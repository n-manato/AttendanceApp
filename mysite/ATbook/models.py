from django.db import models
from django.db.models import Q
from django.utils import timezone
from mylogin.models import User,Subject,Hour
    

class Attend(models.Model):
    type = models.CharField(max_length=50,blank=True)#出席状況
    
    def __str__(self):
        return self.type



#出席情報
class AttendanceInfo(models.Model):
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='related_student',limit_choices_to=Q(groups__name='Student'))
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='related_teacher',limit_choices_to=Q(groups__name='HomeroomTeacher') | Q(groups__name='SubjectTeacher'))
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, related_name='related_subject')
    first_half = models.ForeignKey(Attend, on_delete=models.SET_NULL, null=True, related_name='related_first_half')
    latter_half = models.ForeignKey(Attend, on_delete=models.SET_NULL, null=True, related_name='related_latter_half')
    time = models.ForeignKey(Hour, on_delete=models.SET_NULL, null=True, related_name='related_hourattend')
    date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.student.full_name