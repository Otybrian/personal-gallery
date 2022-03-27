from django.db import models
import pyperclip
# Create your models here.

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()


    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()

    class Meta:
        ordering = ['first_name']

class category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    @classmethod
    def search_by_category(cls, search_term):
        category = cls.objects.filter(name__icontains=search_term)
        return category
    
    def display_searched():
        category=Image.objects.all()
        return category

class location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Image(models.Model):
    name = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ManyToManyField(location)
    editor = models.ForeignKey(Editor)
    category = models.ManyToManyField(category)
    screenshot = models.ImageField(upload_to='images/', blank=True)
    link =  models.CharField(max_length =60)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(self):
        image=Image.objects.get_or_create()
        return image

    @classmethod
    def image_by_id(cls):
        image = Image.objects.get(pk = id)
        return image


    @classmethod
    def copy_link(cls, link):
        link = Image.objects.filter(link)
        pyperclip.copy(link)

 
