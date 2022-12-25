from django.db import models

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=20)
    degree=models.CharField(max_length=20)
    age=models.IntegerChoices()
