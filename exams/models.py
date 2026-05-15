# exams/models.py
# Is file ko pura replace kar do.
# Tumhare current Exam model me ye fields missing hain.
# Iske baad makemigrations aur migrate chalana hoga.

from django.db import models
from students.models import Student
from courses.models import Course


class Exam(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    exam_type = models.CharField(max_length=100)
    marks = models.DecimalField(max_digits=6, decimal_places=2)
    max_marks = models.DecimalField(max_digits=6, decimal_places=2)
    percentage = models.DecimalField(max_digits=6, decimal_places=2)

    date = models.DateField()

    def __str__(self):
        return f"{self.student.name} - {self.exam_type}"