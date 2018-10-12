from django.db import models

# Create your models here.

from django.db import models


class User(models.Model):
    username=models.CharField(max_length=200)
    email = models.EmailField(max_length=255, unique=True)
    country = models.CharField(max_length=50)


class Category(models.Model):
    id = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=20)


class Chinese(models.Model):
    id=models.CharField(max_length=20)
    image=models.FileField(upload_to="E:\photographs\paintings\aaa.jpg",blank= True)
    name=models.CharField(max_length=30)
    desc=models.CharField(max_length=200)
