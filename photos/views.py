from django.shortcuts import render, redirect
import datetime as dt
from .models import Category, Location, Image



# Create your views here.

def gallery(request):
    category = request.GET.get('category')
    if category==None:
        photos=Image.objects.all()
    else:
        photos=Image.objects.filter(category__name = category)
        images = Category.objects.all()
        display={'images':images, 'photos': photos}

    return render(request, 'gallery.html', display)

def search_results(request):


    return render(request, 'search.html')


