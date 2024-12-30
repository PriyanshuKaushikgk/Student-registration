from django.db import models

# Create your models here.

CHOICE = [
    ("male","male"),
    ("female","female"),
    ("other","other"),
]


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    gender = models.CharField(choices=CHOICE, max_length=50)
    image = models.ImageField(upload_to='media',null=True,blank=True)