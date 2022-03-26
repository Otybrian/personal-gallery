
from django.contrib import admin
from .models import Editor,Image,category, location


# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('category','location')
admin.site.register(Editor)
admin.site.register(Image)
admin.site.register(category)
admin.site.register(location)


