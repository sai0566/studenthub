from django.contrib import admin
from attendance.models import Attendance


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'get_roll', 'date', 'status')
    list_filter = ('date', 'status')
    search_fields = ('student__user__username', 'student__roll_number')

    def get_roll(self, obj):
        return obj.student.roll_number

    get_roll.short_description = 'Roll Number'


admin.site.register(Attendance, AttendanceAdmin)