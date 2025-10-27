from django.db import models

# Create your models here.
class Coders(models.Model):
    c_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10,unique=True)
    email=models.CharField(max_length=20,default="user@gmail.com")
    