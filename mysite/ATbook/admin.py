from django.contrib import admin
from .models import AttendanceInfo,Attend
admin.site.register(Attend)

class AttendanceInfoAdmin(admin.ModelAdmin):
    readonly_fields = ("date",)
    list_display = ('student', 'date','time','subject', 'first_half','latter_half')
admin.site.register(AttendanceInfo,AttendanceInfoAdmin)
