from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('courses/', include('courses.urls')),
    path('attendance/', include('attendance.urls')),   # ✅ IMPORTANT
    path('exams/', include('exams.urls')),
    path('timetable/', include('timetable.urls')),
    path('notices/', include('notices.urls')),
    path('fees/', include('fees.urls'), name='fees'),
]