from django.contrib import admin
from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'date', 'status')
    list_filter = ('course', 'date', 'status')
    search_fields = ('student__name',)