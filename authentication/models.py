from django.db import models

# Create your models here.

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=255, unique=True)
    country = models.CharField(max_length=50)


class Food_list(models.Model):
    TYPE_OF_FOOD = (
        ('chinese', 'Chinese'),
        ('indian', 'Indian'),
        ('mexican', 'Mexican'),
        ('italian', 'Italian'),
        ('others', 'Others')
    )

    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=20,
        choices = TYPE_OF_FOOD,
        default ='other',
    )
    image = models.FileField(upload_to="E:\photographs\paintings\aaa.jpg",blank= True)
    desc = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
