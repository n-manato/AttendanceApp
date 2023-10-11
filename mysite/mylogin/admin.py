from django.contrib import admin

# Register your models here.
from .models import User, Department, Subject, Period, Hour, Date
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _

# Register your models here.
@admin.register(Department)
class AdminDepartment(admin.ModelAdmin):
    search_fields = ('name',)
    pass
@admin.register(Subject)
class AdminDepartment(admin.ModelAdmin):
    search_fields = ('subject',)
    pass
@admin.register(Period)
class AdminDepartment(admin.ModelAdmin):
    pass
@admin.register(Hour)
class AdminDepartment(admin.ModelAdmin):
    pass
@admin.register(Date)
class AdminDepartment(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'email', 'departments', 'Subject')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        ('Additional Info', {'fields': ('accidental_absence', 'class_absence', 'sick_absence', 'leaving_early', 'tardiness')}),
    )
    list_display = ('username', 'email', 'full_name', 'is_staff')
    search_fields = ('username', 'full_name', 'email')
    filter_horizontal = ('groups', 'user_permissions')
    filter_vertical = ('departments', 'Subject')

