from django.db import models
from courses.models import Course


class Timetable(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    day = models.CharField(max_length=100)

    time = models.CharField(max_length=100)

    subject_name = models.CharField(max_length=100)

    def __str__(self):

        return self.subject_name