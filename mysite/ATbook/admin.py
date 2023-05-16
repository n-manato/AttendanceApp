from django.contrib import admin
from .models import Student,Teacher,AttendanceInfo,Attend,Period,HourAttend

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Attend)
admin.site.register(Period)
admin.site.register(HourAttend)


class AttendanceInfoAdmin(admin.ModelAdmin):
    readonly_fields = ("date",)
admin.site.register(AttendanceInfo,AttendanceInfoAdmin)