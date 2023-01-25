from django.db import models

# Create your models here.
class Person(models.Model):
    person_name=models.CharField(max_length=25) # called an attribute
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    age=models.IntegerField(default=0)