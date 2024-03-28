from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Student(models.Model):
    student_name=models.CharField( max_length=50)
    mark1=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    mark2=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    mark3=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])


    def __str__(self):
        return self.student_name
    def total(self):
        return self.mark1+self.mark2+self.mark3