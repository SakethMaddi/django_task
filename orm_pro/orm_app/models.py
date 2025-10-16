from django.db import models



# Create your models here.
class Student1(models.Model):
    stu_id=models.IntegerField(primary_key=True)
    stu_name=models.CharField(max_length=50)
    stu_branch=models.CharField(max_length=20)
    stu_mob=models.CharField(max_length=20,unique=True)