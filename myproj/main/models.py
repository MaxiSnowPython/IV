from django.db import models

# Create your models here.
class book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    

class teacher(models.Model):
    
    second_name = models.CharField(max_length=40)
    age = models.IntegerField(max_length=3)
    country = models.CharField(max_length=50)

class test(models.Model):
    text1 = models.CharField(max_length=35)
    text2 = models.CharField(max_length=35)
    text3 = models.CharField(max_length=35)
