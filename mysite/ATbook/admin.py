from django.contrib import admin
from .models import AttendanceInfo,Attend,Total
'''admin.site.register(Attend)

@admin.register(Total)
class AdminTotal(admin.ModelAdmin):
    search_fields = ('student',)
    pass

class AttendanceInfoAdmin(admin.ModelAdmin):
    readonly_fields = ("date",)
    list_display = ('student', 'date','time','subject', 'first_half','latter_half')
admin.site.register(AttendanceInfo,AttendanceInfoAdmin)'''
