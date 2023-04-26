from django.contrib import admin
from .models import Student,Teacher,AttendanceInfo,Attend

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Attend)

class AttendanceInfoAdmin(admin.ModelAdmin):
    readonly_fields = ("date",)
admin.site.register(AttendanceInfo,AttendanceInfoAdmin)