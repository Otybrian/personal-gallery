from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length =30)
    location_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    class Meta:
        ordering = ['name']

class category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Image(models.Model):
    image_id = models.IntegerField(primary_key=True)
    name= models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    location = models.ForeignKey('Location', on_delete=models.PROTECT)
    link= models.CharField(max_length=255)
    category = models.ManyToManyField(category)
    picture = models.ImageField(upload_to='screenshots/', blank=True)
    
    @classmethod
    def display_images(cls):
        image = cls.objects.all()
        return image

    @classmethod
    def days_projects(cls, image_location):
        image = cls.objects.filter(location=image_location)
        return image
    
    @classmethod
    def search_by_category(cls,search_term):
        image = cls.objects.filter(category__icontains=search_term)
        return image

    @classmethod
    def search_by_id(cls, image_id):
        image = cls.objects.filter(id = image_id)
        return image