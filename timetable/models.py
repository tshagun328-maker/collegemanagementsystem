# timetable/models.py

from django.db import models
from courses.models import Course


class Timetable(models.Model):
    YEAR_CHOICES = [
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
        ('4th Year', '4th Year'),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year = models.CharField(max_length=20, choices=YEAR_CHOICES)   # <-- New Column
    subject = models.CharField(max_length=100)
    day = models.CharField(
        max_length=20,
        choices=[
            ('Monday', 'Monday'),
            ('Tuesday', 'Tuesday'),
            ('Wednesday', 'Wednesday'),
            ('Thursday', 'Thursday'),
            ('Friday', 'Friday'),
            ('Saturday', 'Saturday'),
        ]
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.course} - {self.year} - {self.subject}"