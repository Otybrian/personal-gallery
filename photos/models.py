from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

class Location(models.Model):
    name = models.CharField(max_length=50)

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/', blank=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    link = models.CharField(max_length=250)
    location = models.ForeignKey(Category,on_delete=models.CASCADE)
    category =models.ForeignKey(Location,on_delete=models.CASCADE)