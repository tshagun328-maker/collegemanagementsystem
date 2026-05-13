from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    joining_date = models.DateField()
    address = models.TextField()

    def __str__(self):
        return self.name


# Create your models here.
