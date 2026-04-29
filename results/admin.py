from django.contrib import admin

# Register your models here.
from .models import Result


class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'get_roll', 'subject', 'marks', 'total_marks', 'get_status')
    list_filter = ('subject',)
    search_fields = ('student__user__username', 'student__roll_number', 'subject')

    def get_roll(self, obj):
        return obj.student.roll_number

    def get_status(self, obj):
        return obj.subject_status

    get_roll.short_description = 'Roll Number'
    get_status.short_description = 'Status'


admin.site.register(Result, ResultAdmin)