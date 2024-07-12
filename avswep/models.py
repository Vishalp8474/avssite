from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Registeration(models.Model):
  certificate = models.CharField(max_length=50)
  studentname = models.CharField(max_length=255,null=True)
  farthername = models.CharField(max_length=255,null=True)
  mothername = models.CharField(max_length=255,null=True)
  caursename = models.CharField(max_length=255,null=True)
  caursestatus = models.CharField(max_length=255,null=True)
  duration = models.CharField(max_length=255,default="1") 
  date = models.DateField(null=True) 
  photo = models.FileField(upload_to="myimage/",max_length=255,null=True)

  user= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

def __str__(self):
   return f"{self.certificate} {self.studentname} {self.mothername} {self.farthername} {self.caursename} {self.caursestatus}{self.duration} {self.photo}{self.date}"

