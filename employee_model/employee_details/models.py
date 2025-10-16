from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    department=models.CharField(max_length=20)
    emp_id=models.IntegerField()
    salary=models.IntegerField()