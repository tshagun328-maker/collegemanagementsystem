from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll_no', 'course', 'phone', 'email')
    search_fields = ('name', 'roll_no', 'phone', 'email')
    list_filter = ('course',)
    ordering = ('id',)

# Register your models here.
