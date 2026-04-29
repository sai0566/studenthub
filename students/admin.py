from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'roll_number', 'class_name', 'assigned_teacher')
    list_filter = ('class_name', 'assigned_teacher')
    search_fields = ('user__username', 'roll_number')


admin.site.register(Student, StudentAdmin)