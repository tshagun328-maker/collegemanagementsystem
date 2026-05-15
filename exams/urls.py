# exams/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('add/', views.add_exam, name='add_exam'),

    # Edit Exam
    path('edit/<int:id>/', views.edit_exam, name='edit_exam'),

    # Delete Exam
    path('delete/<int:id>/', views.delete_exam, name='delete_exam'),
]