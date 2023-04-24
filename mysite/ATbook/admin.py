from django.contrib import admin
from .models import Student,Teacher,AttendanceInfo

admin.site.register(Teacher)
admin.site.register(Student)#親

class AttendanceInfoAdmin(admin.ModelAdmin):
    readonly_fields = ("date",)
admin.site.register(AttendanceInfo,AttendanceInfoAdmin)