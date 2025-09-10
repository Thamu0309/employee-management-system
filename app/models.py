from django.db import models

# Create your models here.
class Register(models.Model):
    id=models.AutoField(primary_key=True)
    uname=models.CharField(max_length=20)
    mobno=models.IntegerField(null=True)
    email=models.CharField(max_length=20)
    pwrd=models.CharField(max_length=20)

class Empms(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=20)
    fname= models.CharField(max_length=20)
    mobno= models.CharField(max_length=20)
    email= models.CharField(max_length=20)
    dob= models.DateField(max_length=20)
    address= models.CharField(max_length=20)
    exp= models.CharField(max_length=20)
    ctc= models.CharField(max_length=20)