from django.db import models
from students.models import Student
from courses.models import Course

class Exam(models.Model):
    exam_name = models.CharField(max_length=100)
    exam_date = models.DateField()

    def __str__(self):
        return self.exam_name


class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.course.name}"


# Create your models here.
