# fees/models.py
# Tumhare Fee model me ye fields add karni hongi.
# Purana models.py replace kar do.

from django.db import models
from students.models import Student
from courses.models import Course


class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pending_amount = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(max_length=20, default='Pending')
    date = models.DateField()

    def __str__(self):
        return f"{self.student.name} - {self.total_amount}"