from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def search_by_name(cls, search_term):
        category = cls.objects.filter(name__icontains=search_term)
        return category

    @classmethod
    def display_searched():
        category=Image.objects.all()
        return category

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_location(self):
        return self.save()

    def delete_location(self):
        return self.delete()

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/', blank=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    link = models.CharField(max_length=250)
    location = models.ForeignKey(Category,on_delete=models.CASCADE)
    category =models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls):
        image = Image.objects.get_or_create()
        return image

    @classmethod
    def get_image(cls, image_id):
        image = cls.objects.filter(id = image_id)
        return image

    @classmethod
    def search_by_category(cls, search_term):
        image = cls.objects.filter(category__icontains = search_term)
        return image

    @classmethod
    def filter_by_location(cls, location):
        image = cls.objects.filter(location = location)
        return image



