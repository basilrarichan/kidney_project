from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
#Abstract user insted of user in case of variable users
class CustomUser(AbstractUser):
    userType=models.CharField(max_length=50)
    viewpassword=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.username

class Userregistration(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    dob=models.DateTimeField()
    regdate=models.DateField(auto_now_add=True)
    uname=models.CharField(max_length=50,null=True)
    img=models.ImageField(upload_to="profile",null=True)
    def __str__(self):
        return self.name
class Doctorregistration(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    desig=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    dob=models.DateTimeField()
    regdate=models.DateField(auto_now_add=True)
    uname=models.CharField(max_length=50,null=True)
    img=models.ImageField(upload_to="profile",null=True)
    def __str__(self):
        return self.name
class Requestuser(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    status=models.ImageField(upload_to="profile",null=True)
    date=models.DateField(auto_now_add=True)
    # def __str__(self):
    #     return self.requests



class Booking(models.Model):
    councelr=models.ForeignKey(Doctorregistration,on_delete=models.CASCADE)
    usr=models.ForeignKey(Userregistration,on_delete=models.CASCADE)
    request=models.CharField(max_length=100,default="")
    bookingdate=models.CharField(max_length=100)
    dateofbook=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100)
class Authmessage(models.Model):
    usr=models.ForeignKey(Userregistration,on_delete=models.CASCADE)
    messages=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    status=models.CharField(max_length=100)

class Demomodel(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.CharField(max_length=100)