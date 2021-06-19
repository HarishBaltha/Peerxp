from django.db import models

class RegisterModel(models.Model):
    Name=models.CharField(max_length=30)
    Username=models.CharField(max_length=30, unique=True)
    Email=models.EmailField(max_length=20, unique=True)
    Contact=models.IntegerField()
    Password=models.CharField(max_length=15, unique=True)

class LoginModel(models.Model):
    Username=models.CharField(max_length=30, unique=True)
    Password=models.CharField(max_length=15, unique=True)

class TwitterModel(models.Model):
    Username = models.CharField(max_length=30, unique=True)
    Password = models.CharField(max_length=15, unique=True)

class HomeModel(models.Model):
    No = models.AutoField(primary_key=True, default=None)
    Name = models.CharField(max_length=30)
    UserName = models.CharField(max_length=30, unique=True)
    Comments = models.CharField(max_length=200)
    Uploads = models.FileField(upload_to="files/")


